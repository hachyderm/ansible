# Variables

See [defaults/main.yml](defaults/main.yml) for the defaults.

### pgbackrest_exporter_version

Version of the exporter (default `0.22.0`).

### pgbackrest_exporter_os

Operating system of where the exporter will be installed (default `linux`).

### pgbackrest_exporter_arch

Architecture of the system where the exporter will be installed (default
`x86_64`).

### pgbackrest_exporter_download_url

URL used to download the exporter archive (default `https://github.com/woblerr/pgbackrest_exporter/releases/download/v{{ pgbackrest_exporter_version }}/pgbackrest_exporter-{{ pgbackrest_exporter_version }}-{{ pgbackrest_exporter_os }}-{{ pgbackrest_exporter_arch }}.tar.gz"`).

### pgbackrest_exporter_checksum

Checksum of the downloaded archive to avoid supply-chain attack (default
`1562febbb006e96236e30ad0098757724614b2f29f87c1d210fed9083c4c31b5`).

### pgbackrest_exporter_bin

Path to the exporter binary (default `/usr/local/bin/pgbackrest_exporter`).

### pgbackrest_exporter_user

User to create to run the exporter (default `pgbackrest-exp`).

### pgbackrest_exporter_group

Group to create for the user to run the exporter (default `"{{
pgbackrest_exporter_user }}"`).

### pgbackrest_exporter_config_file

Path to the configuration file of pgBackRest
(`/etc/pgbackrest/pgbackrest.conf`).

### pgbackrest_exporter_port

Port to listen for the exporter (default `9854`).

### pgbackrest_exporter_telemetry_path

Route to scrap metrics on the exporter (`/metrics`).
