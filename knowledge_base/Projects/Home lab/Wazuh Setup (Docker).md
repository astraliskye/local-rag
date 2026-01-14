Configuration: https://documentation.wazuh.com/current/deployment-options/docker/wazuh-container.html
Up max map count for Wazuh in Docker Desktop WSL 2 distro
- `wsl -d docker-desktop`
- `sysctl -w vm.max_map_count=262144`
On kali WSL 2 machine
- `git clone https://github.com/wazuh/wazuh-docker.git -b v4.14.1`
- `cd wazuh-docker/single-node`
- Generate certificates
	- `docker compose -f generate-indexer-certs.yml run --rm generator`
- Start container
	- `docker compose up -d`
Change default passwords (one at a time)
- Open `docker-compose.yml`
- Edit all occurrences of `INDEXER_PASSWORD`, `DASHBOARD_PASSWORD`
- `docker compose down`
- Generate hashes for the passwords set for `admin` and `kibanaserver`
	- `docker run --rm -ti wazuh/wazuh-indexer:4.14.1 bash /usr/share/wazuh-indexer/plugins/opensearch-security/tools/hash.sh <plaintext>`
- Put hash in appropriate places in `config/wazuh_indexer/internal_users.yml`
- Enter indexer container
	- docker exec -it <indexer_name> bash
	- Set these variables
		- export INSTALLATION_DIR=/usr/share/wazuh-indexer
		- export CONFIG_DIR=$INSTALLATION_DIR/config
		- CACERT=$CONFIG_DIR/certs/root-ca.pem
		- KEY=$CONFIG_DIR/certs/admin-key.pem
		- CERT=$CONFIG_DIR/certs/admin.pem
		- export JAVA_HOME=/usr/share/wazuh-indexer/jdk
	- Run this command: `bash /usr/share/wazuh-indexer/plugins/opensearch-security/tools/securityadmin.sh -cd $CONFIG_DIR/opensearch-security/ -nhnv -cacert  $CACERT -cert $CERT -key $KEY -p 9200 -icl`
Change password for default API user 
- Change `API_PASSWORD` entries in `docker-compose.yml`
- Change `password` field in `config/wazuh_dashboard/wazuh.yml`
- Restart containers
	- `docker compose down`
	- `docker compose up -d`