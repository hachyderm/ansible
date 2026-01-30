# Variables

See [defaults/main.yml](defaults/main.yml) for the defaults.

### pgbackrest_exporter_version

Version of the exporter (default `0.11.0`).

### pgbouncer_exporter_os

Operating system of where the exporter will be installed (default `linux`).

### pgbouncer_exporter_arch

Architecture of the system where the exporter will be installed (default
`amd64`).

### pgbouncer_exporter_download_url

URL used to download the exporter archive (default
`https://github.com/prometheus-community/pgbouncer_exporter/releases/download/v{{
pgbouncer_exporter_version }}/pgbouncer_exporter-{{ pgbouncer_exporter_version
}}.{{ pgbouncer_exporter_os }}-{{ pgbouncer_exporter_arch }}.tar.gz`).

### pgbouncer_exporter_checksum

Checksum of the downloaded archive to avoid supply-chain attack (default
`de95a3d22141c0f84ac33de07e793c4993410f43d7c10e8ba281559381e031da`).

### pgbouncer_exporter_bin

Path to the exporter binary (default `/usr/local/bin/pgbouncer_exporter`).

### pgbouncer_exporter_user

User to create to run the exporter (default `pgbouncer-exp`).

### pgbouncer_exporter_group

Group to create for the user to run the exporter (default `"{{
pgbouncer_exporter_user }}"`).

### pgbouncer_exporter_port

Port to listen for the exporter (default `9127`).

### pgbouncer_exporter_telemetry_path

Route to scrap metrics on the exporter (`/metrics`).

### pgbouncer_exporter_connection_string

URI to connect to PgBouncer (default
`postgres://postgres:@localhost:6543/pgbouncer?sslmode=disable`).
