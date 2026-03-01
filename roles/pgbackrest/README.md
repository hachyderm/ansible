# Ansible Role: pgBackRest

An Ansible role for installing and configuring
[pgBackRest](https://pgbackrest.org/), a reliable backup and restore solution
for PostgreSQL.

Supported features:

* Standalone deployment
* Distributed deployments (with TLS server)
* PostgreSQL major upgrades

## Requirements

* Ansible 2.18+
* Python 3
* Debian 12 (bookworm)
* `pgdg_repository` role
* `postgresql` role (optional but recommended)


## Table of Content

<!-- ANSIBLE DOCSMITH TOC START -->
* [Role variables](#variables)
  * [`pgbackrest_role`](#variable-pgbackrest_role)
  * [`pgbackrest_settings`](#variable-pgbackrest_settings)
  * [`pgbackrest_schedules`](#variable-pgbackrest_schedules)
  * [`pgbackrest_schedule_full`](#variable-pgbackrest_schedule_full)
  * [`pgbackrest_schedule_diff`](#variable-pgbackrest_schedule_diff)
  * [`pgbackrest_schedule_incr`](#variable-pgbackrest_schedule_incr)
  * [`pgbackrest_schedules_randomized_delay_sec`](#variable-pgbackrest_schedules_randomized_delay_sec)
  * [`pgbackrest_service_after`](#variable-pgbackrest_service_after)
  * [`pgbackrest_notification_command`](#variable-pgbackrest_notification_command)
  * [`pgbackrest_notification_message_start`](#variable-pgbackrest_notification_message_start)
  * [`pgbackrest_notification_message_stop`](#variable-pgbackrest_notification_message_stop)
  * [`pgbackrest_full_install`](#variable-pgbackrest_full_install)
  * [`pgbackrest_additional_groups`](#variable-pgbackrest_additional_groups)
  * [`pgbackrest_user`](#variable-pgbackrest_user)
  * [`pgbackrest_group`](#variable-pgbackrest_group)
  * [`pgbackrest_repositories`](#variable-pgbackrest_repositories)
  * [`pgbackrest_stanzas`](#variable-pgbackrest_stanzas)
  * [`pgbackrest_agent_user`](#variable-pgbackrest_agent_user)
  * [`pgbackrest_agent_group`](#variable-pgbackrest_agent_group)
  * [`pgbackrest_agent_address`](#variable-pgbackrest_agent_address)
  * [`pgbackrest_agent_port`](#variable-pgbackrest_agent_port)
  * [`pgbackrest_agent_tls_ca`](#variable-pgbackrest_agent_tls_ca)
  * [`pgbackrest_agent_tls_ca_file`](#variable-pgbackrest_agent_tls_ca_file)
  * [`pgbackrest_agent_tls_cert`](#variable-pgbackrest_agent_tls_cert)
  * [`pgbackrest_agent_tls_cert_file`](#variable-pgbackrest_agent_tls_cert_file)
  * [`pgbackrest_agent_tls_key`](#variable-pgbackrest_agent_tls_key)
  * [`pgbackrest_agent_tls_key_file`](#variable-pgbackrest_agent_tls_key_file)
  * [`pgbackrest_agent_stanzas`](#variable-pgbackrest_agent_stanzas)
  * [`pgbackrest_agent_allowed_users`](#variable-pgbackrest_agent_allowed_users)
  * [`pgbackrest_agent_repositories`](#variable-pgbackrest_agent_repositories)
  * [`pgbackrest_server_user`](#variable-pgbackrest_server_user)
  * [`pgbackrest_server_user_home`](#variable-pgbackrest_server_user_home)
  * [`pgbackrest_server_group`](#variable-pgbackrest_server_group)
  * [`pgbackrest_server_address`](#variable-pgbackrest_server_address)
  * [`pgbackrest_server_port`](#variable-pgbackrest_server_port)
  * [`pgbackrest_server_tls_ca`](#variable-pgbackrest_server_tls_ca)
  * [`pgbackrest_server_tls_ca_file`](#variable-pgbackrest_server_tls_ca_file)
  * [`pgbackrest_server_tls_cert`](#variable-pgbackrest_server_tls_cert)
  * [`pgbackrest_server_tls_cert_file`](#variable-pgbackrest_server_tls_cert_file)
  * [`pgbackrest_server_tls_key`](#variable-pgbackrest_server_tls_key)
  * [`pgbackrest_server_tls_key_file`](#variable-pgbackrest_server_tls_key_file)
  * [`pgbackrest_server_repositories`](#variable-pgbackrest_server_repositories)
  * [`pgbackrest_server_stanzas`](#variable-pgbackrest_server_stanzas)
  * [`pgbackrest_server_allowed_users`](#variable-pgbackrest_server_allowed_users)
  * [`pgbackrest_server_lock_path`](#variable-pgbackrest_server_lock_path)
<!-- ANSIBLE DOCSMITH TOC END -->
<!-- ANSIBLE DOCSMITH MAIN START -->

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description (abstract) |
|----------|------|----------|---------|------------------------|
| `pgbackrest_role` | `str` | No | `"standalone"` | Role of the pgBackRest instance on the server.<br><br>C(standalone) to run everything locally.<br><br>C(server) to start a TLS server and orchestrate backup policies.<br><br>C(agent) to start a TLS server to receive operations from the […](#variable-pgbackrest_role) |
| `pgbackrest_settings` | `dict` | No | N/A | Dictionary of custom settings.<br><br>The key is the setting name.<br><br>The value is the setting value.<br><br>See L(General Options,https://pgbackrest.org/configuration.html#section-general). |
| `pgbackrest_schedules` | `dict` | No | N/A | DEPRECATED.<br><br>Use C(pgbackrest_schedule_full), C(pgbackrest_schedule_diff) and C(pgbackrest_schedule_incr) instead.<br><br>Dictionary of backup schedules.<br><br>The key is the backup type (C(full) or C(diff)).<br><br>The value is a dict of […](#variable-pgbackrest_schedules) |
| `pgbackrest_schedule_full` | `str` | No | N/A | When to start full backups.<br><br>See L(OnCalendar,https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html#OnCalendar=).<br><br>See L(Calendar […](#variable-pgbackrest_schedule_full) |
| `pgbackrest_schedule_diff` | `str` | No | N/A | When to start differential backups.<br><br>See L(OnCalendar,https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html#OnCalendar=).<br><br>See L(Calendar […](#variable-pgbackrest_schedule_diff) |
| `pgbackrest_schedule_incr` | `str` | No | N/A | When to start incremental backups.<br><br>See L(OnCalendar,https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html#OnCalendar=).<br><br>See L(Calendar […](#variable-pgbackrest_schedule_incr) |
| `pgbackrest_schedules_randomized_delay_sec` | `int` | No | N/A | Random number of seconds to wait before starting backup services. |
| `pgbackrest_service_after` | `list` | No | N/A | List of systemd units to wait before starting pgBackRest. |
| `pgbackrest_notification_command` | `str` | No | N/A | Command to execute when a pgBackRest backup command is performed.<br><br>The command takes two positional arguments.<br><br>1. the C(pgBackRest) string to tell who's runing the command.<br><br>2. a C(message) to tell what is happening (replaced by […](#variable-pgbackrest_notification_command) |
| `pgbackrest_notification_message_start` | `str` | No | `"starting"` | Message sent to the notification command when a backup command is starting. |
| `pgbackrest_notification_message_stop` | `str` | No | `"done"` | Message sent to the notification command when a backup command is stopping. |
| `pgbackrest_full_install` | `bool` | No | `true` | Enable tasks that are part of a circular dependency with the C(hachyderm.general.postgresql) role.<br><br>Checking configuration forces a WAL to be archived so a working PostgreSQL instance is required.<br><br>But, if PostgreSQL is deployed with the […](#variable-pgbackrest_full_install) |
| `pgbackrest_additional_groups` | `list` | No | N/A | List of groups to append to the operating system user. |
| `pgbackrest_user` | `str` | No | `"postgres"` | Operating system user for a standalone deployment. |
| `pgbackrest_group` | `str` | No | `"postgres"` | Operating system group for a standalone deployment. |
| `pgbackrest_repositories` | `list` | No | N/A | List of repositories in a standalone deployment.<br><br>The repository index will be automatically generated.<br><br>See L(Repository Options,https://pgbackrest.org/configuration.html#section-repository). |
| `pgbackrest_stanzas` | `dict` | No | N/A | Dictionary of stanzas to create in a standalone deployment.<br><br>The repository index will be automatically generated.<br><br>See L(Stanza Options,https://pgbackrest.org/configuration.html#section-stanza). |
| `pgbackrest_agent_user` | `str` | No | `"postgres"` | Operating system user for an agent. |
| `pgbackrest_agent_group` | `str` | No | `"postgres"` | Operating system group for an agent. |
| `pgbackrest_agent_address` | `str` | No | `"localhost"` | Address to listen for an agent.<br><br>See L(TLS Server Address Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-address). |
| `pgbackrest_agent_port` | `int` | No | `8432` | Address to listen for an agent.<br><br>See L(TLS Server Port Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-port). |
| `pgbackrest_agent_tls_ca` | `str` | No | N/A | Content of a Certificate Authority (CA) to verify the authenticity of TLS certificates for an agent.<br><br>Use the same CA for agent and server.<br><br>If defined, the content will be written in C(pgbackrest_agent_tls_ca_file).<br><br>See L(TLS […](#variable-pgbackrest_agent_tls_ca) |
| `pgbackrest_agent_tls_ca_file` | `path` | No | `"/etc/pgbackrest/ca.crt"` | Path to the TLS server certificate authorities for an agent.<br><br>For certificates signed by a trusted CA (like Let's Encrypt), use C(/etc/ssl/certs/ca-certificates.crt).<br><br>See L(TLS Server Certificate Authorities […](#variable-pgbackrest_agent_tls_ca_file) |
| `pgbackrest_agent_tls_cert` | `str` | No | N/A | Content of the TLS server certificate for an agent.<br><br>See L(TLS Server Certificate Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-cert-file).<br><br>Generate a test cert (and key) with C(openssl req -new -nodes […](#variable-pgbackrest_agent_tls_cert) |
| `pgbackrest_agent_tls_cert_file` | `path` | No | `"/etc/pgbackrest/server.crt"` | Path to the TLS server certificate for an agent.<br><br>See L(TLS Server Certificate Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-cert-file). |
| `pgbackrest_agent_tls_key` | `str` | No | N/A | Content of the TLS server key for an agent.<br><br>If defined, the content will be written in C(pgbackrest_agent_tls_key_file).<br><br>See L(TLS Server Key Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-key-file). |
| `pgbackrest_agent_tls_key_file` | `path` | No | `"/etc/pgbackrest/server.key"` | Path to the TLS server key file for an agent.<br><br>See L(TLS Server Key Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-key-file). |
| `pgbackrest_agent_stanzas` | `dict` | No | N/A | Dictionary of stanzas supported by an agent.<br><br>The key is the name of each stanza.<br><br>The value is a list of stanza options.<br><br>The server index will be automatically generated.<br><br>See L(Stanza […](#variable-pgbackrest_agent_stanzas) |
| `pgbackrest_agent_allowed_users` | `dict` | No | N/A | Dictionary of allowed users (server) on the agent.<br><br>The key is the hostname.<br><br>The value is the stanza name.<br><br>See L(TLS Server Authorized Clients […](#variable-pgbackrest_agent_allowed_users) |
| `pgbackrest_agent_repositories` | `list` | No | `[{'host': 'localhost', 'port': 8432, 'user': 'pgbackrest', 'config': '/etc/pgbackrest-server/pgbackrest.conf'}]` | List of agent to repositories (server) communication.<br><br>All repositories must be declared.<br><br>If pgBackRest is supposed to send backups to multiple object storage or filesystems, create a list of the size of the number of server repositories […](#variable-pgbackrest_agent_repositories) |
| `pgbackrest_server_user` | `str` | No | `"pgbackrest"` | Operating system user for a server. |
| `pgbackrest_server_user_home` | `path` | No | `"/var/lib/pgbackrest"` | Home of the operating system user for a server. |
| `pgbackrest_server_group` | `str` | No | `"pgbackrest"` | Operating system group for a server. |
| `pgbackrest_server_address` | `str` | No | `"localhost"` | Address to listen for a server.<br><br>See L(TLS Server Address Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-address). |
| `pgbackrest_server_port` | `int` | No | `8432` | Port to listen for a server.<br><br>See L(TLS Server Port Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-port). |
| `pgbackrest_server_tls_ca` | `str` | No | N/A | Content of a Certificate Authority (CA) to verify the authenticity of TLS certificates for a server.<br><br>Use the same CA for agent and server.<br><br>If defined, the content will be written in C(pgbackrest_server_tls_ca_file).<br><br>See L(TLS […](#variable-pgbackrest_server_tls_ca) |
| `pgbackrest_server_tls_ca_file` | `path` | No | `"/etc/pgbackrest-server/ca.crt"` | Path to the TLS server certificate authorities for a server.<br><br>See L(TLS Server Certificate Authorities Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-ca-file). |
| `pgbackrest_server_tls_cert` | `str` | No | N/A | Content of the TLS server certificate for a server.<br><br>When C(pgbackrest_role) is C(both), use the same TLS cert for agent and server.<br><br>If defined, the content will be written in C(pgbackrest_server_tls_cert_file).<br><br>See L(TLS Server […](#variable-pgbackrest_server_tls_cert) |
| `pgbackrest_server_tls_cert_file` | `path` | No | `"/etc/pgbackrest-server/server.crt"` | Path to the TLS server certificate for a server.<br><br>See L(TLS Server Certificate Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-cert-file). |
| `pgbackrest_server_tls_key` | `str` | No | N/A | Content of the TLS server key for a server.<br><br>When C(pgbackrest_role) is C(both), use the same TLS key for agent and server.<br><br>If defined, the content will be written in C(pgbackrest_server_tls_key_file).<br><br>See L(TLS Server Key […](#variable-pgbackrest_server_tls_key) |
| `pgbackrest_server_tls_key_file` | `path` | No | `"/etc/pgbackrest-server/server.key"` | Path to the TLS server key file for a server.<br><br>See L(TLS Server Key Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-key-file). |
| `pgbackrest_server_repositories` | `list` | No | N/A | List of repositories.<br><br>See L(Repository Options,https://pgbackrest.org/configuration.html#section-repository). |
| `pgbackrest_server_stanzas` | `dict` | No | N/A | Dictionary of stanzas to create on a server.<br><br>The key is the stanza name.<br><br>The value is a list of repositories.<br><br>The server index will be automatically generated.<br><br>See L(Stanza […](#variable-pgbackrest_server_stanzas) |
| `pgbackrest_server_allowed_users` | `dict` | No | N/A | Dictionary of allowed users (agents) on the server.<br><br>The key is the hostname.<br><br>The value is the stanza name.<br><br>Names must be included in the TLS certificate and resolvable by DNS.<br><br>See L(TLS Server Authorized Clients […](#variable-pgbackrest_server_allowed_users) |
| `pgbackrest_server_lock_path` | `path` | No | `"/tmp/pgbackrest-server"` | Path where lock files are stored on the server.<br><br>See L(Lock Path Option,https://pgbackrest.org/configuration.html#section-general/option-lock-path). |

### `pgbackrest_role`<a id="variable-pgbackrest_role"></a>

[*⇑ Back to ToC ⇑*](#toc)

Role of the pgBackRest instance on the server.

C(standalone) to run everything locally.

C(server) to start a TLS server and orchestrate backup policies.

C(agent) to start a TLS server to receive operations from the server.

C(both) to configure a server and an agent on the same host.

- **Type**: `str`
- **Required**: No
- **Default**: `"standalone"`
- **Choices**: `standalone`, `server`, `agent`, `both`



### `pgbackrest_settings`<a id="variable-pgbackrest_settings"></a>

[*⇑ Back to ToC ⇑*](#toc)

Dictionary of custom settings.

The key is the setting name.

The value is the setting value.

See L(General Options,https://pgbackrest.org/configuration.html#section-general).

- **Type**: `dict`
- **Required**: No



### `pgbackrest_schedules`<a id="variable-pgbackrest_schedules"></a>

[*⇑ Back to ToC ⇑*](#toc)

DEPRECATED.

Use C(pgbackrest_schedule_full), C(pgbackrest_schedule_diff) and C(pgbackrest_schedule_incr) instead.

Dictionary of backup schedules.

The key is the backup type (C(full) or C(diff)).

The value is a dict of systemd timer settings (see L(systemd.timer,https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html)).

- **Type**: `dict`
- **Required**: No



### `pgbackrest_schedule_full`<a id="variable-pgbackrest_schedule_full"></a>

[*⇑ Back to ToC ⇑*](#toc)

When to start full backups.

See L(OnCalendar,https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html#OnCalendar=).

See L(Calendar Events,https://www.freedesktop.org/software/systemd/man/latest/systemd.time.html#Calendar%20Events).

- **Type**: `str`
- **Required**: No



### `pgbackrest_schedule_diff`<a id="variable-pgbackrest_schedule_diff"></a>

[*⇑ Back to ToC ⇑*](#toc)

When to start differential backups.

See L(OnCalendar,https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html#OnCalendar=).

See L(Calendar Events,https://www.freedesktop.org/software/systemd/man/latest/systemd.time.html#Calendar%20Events).

- **Type**: `str`
- **Required**: No



### `pgbackrest_schedule_incr`<a id="variable-pgbackrest_schedule_incr"></a>

[*⇑ Back to ToC ⇑*](#toc)

When to start incremental backups.

See L(OnCalendar,https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html#OnCalendar=).

See L(Calendar Events,https://www.freedesktop.org/software/systemd/man/latest/systemd.time.html#Calendar%20Events).

- **Type**: `str`
- **Required**: No



### `pgbackrest_schedules_randomized_delay_sec`<a id="variable-pgbackrest_schedules_randomized_delay_sec"></a>

[*⇑ Back to ToC ⇑*](#toc)

Random number of seconds to wait before starting backup services.

- **Type**: `int`
- **Required**: No



### `pgbackrest_service_after`<a id="variable-pgbackrest_service_after"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of systemd units to wait before starting pgBackRest.

- **Type**: `list`
- **Required**: No
- **List Elements**: `str`



### `pgbackrest_notification_command`<a id="variable-pgbackrest_notification_command"></a>

[*⇑ Back to ToC ⇑*](#toc)

Command to execute when a pgBackRest backup command is performed.

The command takes two positional arguments.

1. the C(pgBackRest) string to tell who's runing the command.

2. a C(message) to tell what is happening (replaced by C(pgbackrest_notification_message_start) and C(pgbackrest_notification_message_stop)).

- **Type**: `str`
- **Required**: No



### `pgbackrest_notification_message_start`<a id="variable-pgbackrest_notification_message_start"></a>

[*⇑ Back to ToC ⇑*](#toc)

Message sent to the notification command when a backup command is starting.

- **Type**: `str`
- **Required**: No
- **Default**: `"starting"`



### `pgbackrest_notification_message_stop`<a id="variable-pgbackrest_notification_message_stop"></a>

[*⇑ Back to ToC ⇑*](#toc)

Message sent to the notification command when a backup command is stopping.

- **Type**: `str`
- **Required**: No
- **Default**: `"done"`



### `pgbackrest_full_install`<a id="variable-pgbackrest_full_install"></a>

[*⇑ Back to ToC ⇑*](#toc)

Enable tasks that are part of a circular dependency with the C(hachyderm.general.postgresql) role.

Checking configuration forces a WAL to be archived so a working PostgreSQL instance is required.

But, if PostgreSQL is deployed with the pgbackrest binary for the restore command, the service may not start because it requires pgBackRest to be fully working.

Same for stanza creation.

The C(pgbackrest_full_install) variable can be disabled to ignore all the tasks that are part of the circular dependency issue.

- **Type**: `bool`
- **Required**: No
- **Default**: `true`



### `pgbackrest_additional_groups`<a id="variable-pgbackrest_additional_groups"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of groups to append to the operating system user.

- **Type**: `list`
- **Required**: No
- **List Elements**: `str`



### `pgbackrest_user`<a id="variable-pgbackrest_user"></a>

[*⇑ Back to ToC ⇑*](#toc)

Operating system user for a standalone deployment.

- **Type**: `str`
- **Required**: No
- **Default**: `"postgres"`



### `pgbackrest_group`<a id="variable-pgbackrest_group"></a>

[*⇑ Back to ToC ⇑*](#toc)

Operating system group for a standalone deployment.

- **Type**: `str`
- **Required**: No
- **Default**: `"postgres"`



### `pgbackrest_repositories`<a id="variable-pgbackrest_repositories"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of repositories in a standalone deployment.

The repository index will be automatically generated.

See L(Repository Options,https://pgbackrest.org/configuration.html#section-repository).

- **Type**: `list`
- **Required**: No
- **List Elements**: `dict`



### `pgbackrest_stanzas`<a id="variable-pgbackrest_stanzas"></a>

[*⇑ Back to ToC ⇑*](#toc)

Dictionary of stanzas to create in a standalone deployment.

The repository index will be automatically generated.

See L(Stanza Options,https://pgbackrest.org/configuration.html#section-stanza).

- **Type**: `dict`
- **Required**: No



### `pgbackrest_agent_user`<a id="variable-pgbackrest_agent_user"></a>

[*⇑ Back to ToC ⇑*](#toc)

Operating system user for an agent.

- **Type**: `str`
- **Required**: No
- **Default**: `"postgres"`



### `pgbackrest_agent_group`<a id="variable-pgbackrest_agent_group"></a>

[*⇑ Back to ToC ⇑*](#toc)

Operating system group for an agent.

- **Type**: `str`
- **Required**: No
- **Default**: `"postgres"`



### `pgbackrest_agent_address`<a id="variable-pgbackrest_agent_address"></a>

[*⇑ Back to ToC ⇑*](#toc)

Address to listen for an agent.

See L(TLS Server Address Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-address).

- **Type**: `str`
- **Required**: No
- **Default**: `"localhost"`



### `pgbackrest_agent_port`<a id="variable-pgbackrest_agent_port"></a>

[*⇑ Back to ToC ⇑*](#toc)

Address to listen for an agent.

See L(TLS Server Port Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-port).

- **Type**: `int`
- **Required**: No
- **Default**: `8432`



### `pgbackrest_agent_tls_ca`<a id="variable-pgbackrest_agent_tls_ca"></a>

[*⇑ Back to ToC ⇑*](#toc)

Content of a Certificate Authority (CA) to verify the authenticity of TLS certificates for an agent.

Use the same CA for agent and server.

If defined, the content will be written in C(pgbackrest_agent_tls_ca_file).

See L(TLS Server Certificate Authorities Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-ca-file).

Generate a test CA with C(openssl req -new -x509 -days 3650 -nodes -out ca.crt -keyout ca.key -subj "/CN=ca").

- **Type**: `str`
- **Required**: No



### `pgbackrest_agent_tls_ca_file`<a id="variable-pgbackrest_agent_tls_ca_file"></a>

[*⇑ Back to ToC ⇑*](#toc)

Path to the TLS server certificate authorities for an agent.

For certificates signed by a trusted CA (like Let's Encrypt), use C(/etc/ssl/certs/ca-certificates.crt).

See L(TLS Server Certificate Authorities Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-ca-file).

- **Type**: `path`
- **Required**: No
- **Default**: `"/etc/pgbackrest/ca.crt"`



### `pgbackrest_agent_tls_cert`<a id="variable-pgbackrest_agent_tls_cert"></a>

[*⇑ Back to ToC ⇑*](#toc)

Content of the TLS server certificate for an agent.

See L(TLS Server Certificate Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-cert-file).

Generate a test cert (and key) with C(openssl req -new -nodes -out primary.csr -keyout primary.key -subj "/CN=primary") and C(openssl x509 -req -in primary.csr -days 3650 -CA ca.crt -CAkey ca.key -CAcreateserial -out primary.crt) where C(primary) is the resolvable hostname of the agent.

- **Type**: `str`
- **Required**: No



### `pgbackrest_agent_tls_cert_file`<a id="variable-pgbackrest_agent_tls_cert_file"></a>

[*⇑ Back to ToC ⇑*](#toc)

Path to the TLS server certificate for an agent.

See L(TLS Server Certificate Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-cert-file).

- **Type**: `path`
- **Required**: No
- **Default**: `"/etc/pgbackrest/server.crt"`



### `pgbackrest_agent_tls_key`<a id="variable-pgbackrest_agent_tls_key"></a>

[*⇑ Back to ToC ⇑*](#toc)

Content of the TLS server key for an agent.

If defined, the content will be written in C(pgbackrest_agent_tls_key_file).

See L(TLS Server Key Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-key-file).

- **Type**: `str`
- **Required**: No



### `pgbackrest_agent_tls_key_file`<a id="variable-pgbackrest_agent_tls_key_file"></a>

[*⇑ Back to ToC ⇑*](#toc)

Path to the TLS server key file for an agent.

See L(TLS Server Key Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-key-file).

- **Type**: `path`
- **Required**: No
- **Default**: `"/etc/pgbackrest/server.key"`



### `pgbackrest_agent_stanzas`<a id="variable-pgbackrest_agent_stanzas"></a>

[*⇑ Back to ToC ⇑*](#toc)

Dictionary of stanzas supported by an agent.

The key is the name of each stanza.

The value is a list of stanza options.

The server index will be automatically generated.

See L(Stanza Options,https://pgbackrest.org/configuration.html#section-stanza).

- **Type**: `dict`
- **Required**: No



### `pgbackrest_agent_allowed_users`<a id="variable-pgbackrest_agent_allowed_users"></a>

[*⇑ Back to ToC ⇑*](#toc)

Dictionary of allowed users (server) on the agent.

The key is the hostname.

The value is the stanza name.

See L(TLS Server Authorized Clients Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-auth).

- **Type**: `dict`
- **Required**: No



### `pgbackrest_agent_repositories`<a id="variable-pgbackrest_agent_repositories"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of agent to repositories (server) communication.

All repositories must be declared.

If pgBackRest is supposed to send backups to multiple object storage or filesystems, create a list of the size of the number of server repositories (C(pgbackrest_server_repositories)).

Even if the content is repeated.

The repository index will be automatically generated.

See L(Repository Options,https://pgbackrest.org/configuration.html#section-repository).

- **Type**: `list`
- **Required**: No
- **Default**: `[{'host': 'localhost', 'port': 8432, 'user': 'pgbackrest', 'config': '/etc/pgbackrest-server/pgbackrest.conf'}]`
- **List Elements**: `dict`



### `pgbackrest_server_user`<a id="variable-pgbackrest_server_user"></a>

[*⇑ Back to ToC ⇑*](#toc)

Operating system user for a server.

- **Type**: `str`
- **Required**: No
- **Default**: `"pgbackrest"`



### `pgbackrest_server_user_home`<a id="variable-pgbackrest_server_user_home"></a>

[*⇑ Back to ToC ⇑*](#toc)

Home of the operating system user for a server.

- **Type**: `path`
- **Required**: No
- **Default**: `"/var/lib/pgbackrest"`



### `pgbackrest_server_group`<a id="variable-pgbackrest_server_group"></a>

[*⇑ Back to ToC ⇑*](#toc)

Operating system group for a server.

- **Type**: `str`
- **Required**: No
- **Default**: `"pgbackrest"`



### `pgbackrest_server_address`<a id="variable-pgbackrest_server_address"></a>

[*⇑ Back to ToC ⇑*](#toc)

Address to listen for a server.

See L(TLS Server Address Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-address).

- **Type**: `str`
- **Required**: No
- **Default**: `"localhost"`



### `pgbackrest_server_port`<a id="variable-pgbackrest_server_port"></a>

[*⇑ Back to ToC ⇑*](#toc)

Port to listen for a server.

See L(TLS Server Port Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-port).

- **Type**: `int`
- **Required**: No
- **Default**: `8432`



### `pgbackrest_server_tls_ca`<a id="variable-pgbackrest_server_tls_ca"></a>

[*⇑ Back to ToC ⇑*](#toc)

Content of a Certificate Authority (CA) to verify the authenticity of TLS certificates for a server.

Use the same CA for agent and server.

If defined, the content will be written in C(pgbackrest_server_tls_ca_file).

See L(TLS Server Certificate Authorities Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-ca-file).

- **Type**: `str`
- **Required**: No



### `pgbackrest_server_tls_ca_file`<a id="variable-pgbackrest_server_tls_ca_file"></a>

[*⇑ Back to ToC ⇑*](#toc)

Path to the TLS server certificate authorities for a server.

See L(TLS Server Certificate Authorities Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-ca-file).

- **Type**: `path`
- **Required**: No
- **Default**: `"/etc/pgbackrest-server/ca.crt"`



### `pgbackrest_server_tls_cert`<a id="variable-pgbackrest_server_tls_cert"></a>

[*⇑ Back to ToC ⇑*](#toc)

Content of the TLS server certificate for a server.

When C(pgbackrest_role) is C(both), use the same TLS cert for agent and server.

If defined, the content will be written in C(pgbackrest_server_tls_cert_file).

See L(TLS Server Certificate Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-cert-file).

Generate a test cert (and key) with C(openssl req -new -nodes -out server.csr -keyout server.key -subj "/CN=server") and C(openssl x509 -req -in server.csr -days 3650 -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt) where C(server) is the resolvable hostname of the backup server.

- **Type**: `str`
- **Required**: No



### `pgbackrest_server_tls_cert_file`<a id="variable-pgbackrest_server_tls_cert_file"></a>

[*⇑ Back to ToC ⇑*](#toc)

Path to the TLS server certificate for a server.

See L(TLS Server Certificate Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-cert-file).

- **Type**: `path`
- **Required**: No
- **Default**: `"/etc/pgbackrest-server/server.crt"`



### `pgbackrest_server_tls_key`<a id="variable-pgbackrest_server_tls_key"></a>

[*⇑ Back to ToC ⇑*](#toc)

Content of the TLS server key for a server.

When C(pgbackrest_role) is C(both), use the same TLS key for agent and server.

If defined, the content will be written in C(pgbackrest_server_tls_key_file).

See L(TLS Server Key Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-key-file).

- **Type**: `str`
- **Required**: No



### `pgbackrest_server_tls_key_file`<a id="variable-pgbackrest_server_tls_key_file"></a>

[*⇑ Back to ToC ⇑*](#toc)

Path to the TLS server key file for a server.

See L(TLS Server Key Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-key-file).

- **Type**: `path`
- **Required**: No
- **Default**: `"/etc/pgbackrest-server/server.key"`



### `pgbackrest_server_repositories`<a id="variable-pgbackrest_server_repositories"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of repositories.

See L(Repository Options,https://pgbackrest.org/configuration.html#section-repository).

- **Type**: `list`
- **Required**: No
- **List Elements**: `dict`



### `pgbackrest_server_stanzas`<a id="variable-pgbackrest_server_stanzas"></a>

[*⇑ Back to ToC ⇑*](#toc)

Dictionary of stanzas to create on a server.

The key is the stanza name.

The value is a list of repositories.

The server index will be automatically generated.

See L(Stanza Options,https://pgbackrest.org/configuration.html#section-stanza).

- **Type**: `dict`
- **Required**: No



### `pgbackrest_server_allowed_users`<a id="variable-pgbackrest_server_allowed_users"></a>

[*⇑ Back to ToC ⇑*](#toc)

Dictionary of allowed users (agents) on the server.

The key is the hostname.

The value is the stanza name.

Names must be included in the TLS certificate and resolvable by DNS.

See L(TLS Server Authorized Clients Option,https://pgbackrest.org/configuration.html#section-server/option-tls-server-auth).

- **Type**: `dict`
- **Required**: No



### `pgbackrest_server_lock_path`<a id="variable-pgbackrest_server_lock_path"></a>

[*⇑ Back to ToC ⇑*](#toc)

Path where lock files are stored on the server.

See L(Lock Path Option,https://pgbackrest.org/configuration.html#section-general/option-lock-path).

- **Type**: `path`
- **Required**: No
- **Default**: `"/tmp/pgbackrest-server"`




<!-- ANSIBLE DOCSMITH MAIN END -->

## Example

### Standalone

PostgreSQL and pgBackRest on the same host.

Variables:

```yaml
postgresql_version: 18
postgresql_superuser_password: CHANGEME
postgresql_manage_pgpass: true
postgresql_archive_command: 'pgbackrest --stanza=main --log-level-console=warn archive-push %p'
postgresql_restore_command: 'pgbackrest --stanza=main --log-level-console=warn archive-get %f "%p"'

pgbackrest_repositories:
  - path: /var/lib/pgbackrest
    cipher-pass: CHANGEME
    cipher-type: aes-256-cbc
    retention-full-type: time
    retention-full: 14
    retention-diff: 3
    bundle: y
pgbackrest_stanzas:
  main:
   - pg-path: "/var/lib/postgresql/{{ postgresql_version }}/main"
     pg-host-port: 5432
pgbackrest_schedule_full: "Mon *-*-* 4:30:00"
pgbackrest_schedule_diff: "Tue..Sun *-*-* 4:30:00"
pgbackrest_schedules_randomized_delay_sec: 1800
```

Playbook:

```yaml
- name: Install minimal pgBackRest and PostgreSQL
  hosts: all
  become: true
  roles:
    - hachyderm.general.pgbackrest
    - hachyderm.general.postgresql
  vars:
    pgbackrest_full_install: false

- name: Finalize pgBackRest configuration
  hosts: all
  become: true
  roles:
    - hachyderm.general.pgbackrest
```

### Two nodes

PostgreSQL primary replicating to a replica with pgBackRest repository deployed
on the replica.

Configure PostgreSQL replication (see [PostgreSQL
role](../postgresql/README.md]).

Common PostgreSQL variables:

```yaml
postgresql_version: 18
postgresql_superuser_password: CHANGEME
postgresql_listen_addresses:
  - '*'
postgresql_manage_replication: true
postgresql_replication_username: repl
postgresql_replication_password: CHANGEME
postgresql_replication_network: 192.168.0.0/24
postgresql_manage_pgpass: true
postgresql_archive_command: 'pgbackrest --stanza=main --log-level-console=warn archive-push %p'
postgresql_restore_command: 'pgbackrest --stanza=main --log-level-console=warn archive-get %f "%p"'
```

PostgreSQL variables for the replica:

```yaml
postgresql_instance_role: replica
postgresql_primary_host: 192.168.0.1
```

Generate TLS certificates:

> [!WARNING]
>
> For testing purpose only

```
openssl req -new -x509 -days 3650 -nodes -out ca.crt -keyout ca.key -subj "/CN=ca"
openssl req -new -nodes -out primary.csr -keyout primary.key -subj "/CN=primary"
openssl x509 -req -in primary.csr -days 3650 -CA ca.crt -CAkey ca.key -CAcreateserial -out primary.crt
openssl req -new -nodes -out replica.csr -keyout replica.key -subj "/CN=replica"
openssl x509 -req -in replica.csr -days 3650 -CA ca.crt -CAkey ca.key -CAcreateserial -out replica.crt
```

Common variables:

```yaml
pgbackrest_agent_address: 0.0.0.0
pgbackrest_agent_port: 8433
pgbackrest_agent_allowed_users:
  replica: main
pgbackrest_agent_repositories:
  - host: replica
    port: 8432
    user: pgbackrest
    config: /etc/pgbackrest-server/pgbackrest.conf
pgbackrest_agent_stanzas:
  main:
    - pg-path: "/var/lib/postgresql/{{ postgresql_version }}/main"
```

Variables for the primary:

```yaml
pgbackrest_role: agent
pgbackrest_agent_tls_ca: |
  [content of ca.crt]
pgbackrest_agent_tls_cert: |
  [content of primary.crt]
pgbackrest_agent_tls_key: |
  [content of primary.key]
```

Variables for the replica:

```yaml
pgbackrest_role: both
pgbackrest_server_tls_ca: &pgbackrest_ca |
  [content of ca.crt]
pgbackrest_server_tls_cert: &pgbackrest_cert |
  [content of replica.crt]
pgbackrest_server_tls_key: &pgbackrest_key |
  [content of replica.key]
pgbackrest_agent_tls_ca: *pgbackrest_ca
pgbackrest_agent_tls_cert: *pgbackrest_cert
pgbackrest_agent_tls_key: *pgbackrest_key
pgbackrest_server_address: 0.0.0.0
pgbackrest_server_port: 8432
pgbackrest_server_allowed_users:
  primary: main
  replica: main
pgbackrest_server_repositories:
  - path: /var/lib/pgbackrest
    cipher-pass: CHANGEME
    cipher-type: aes-256-cbc
    retention-full-type: time
    retention-full: 14
    retention-diff: 3
    bundle: y
pgbackrest_server_stanzas:
  main:
    - pg-host: primary
      pg-host-port: 8433
      pg-path: "/var/lib/postgresql/{{ postgresql_version }}/main"
    - pg-host: replica
      pg-host-port: 8433
      pg-path: "/var/lib/postgresql/{{ postgresql_version }}/main"
pgbackrest_schedule_full: "Mon *-*-* 4:30:00"
pgbackrest_schedule_diff: "Tue..Sun *-*-* 4:30:00"
pgbackrest_schedules_randomized_delay_sec: 1800
```

Playbook:

```yaml
- name: Prepare servers
  hosts: all
  become: true
  tasks:
    - name: Add entries to /etc/hosts
      ansible.builtin.blockinfile:
        path: /etc/hosts
        block: |
          192.168.0.1 primary
          192.168.0.2 replica

- name: Install minimal pgBackRest and PostgreSQL
  hosts: all
  become: true
  roles:
    - hachyderm.general.pgbackrest
    - hachyderm.general.postgresql
  vars:
    pgbackrest_full_install: false

- name: Finalize pgBackRest configuration
  hosts: all
  become: true
  roles:
    - hachyderm.general.pgbackrest
```

Create a backup and verify on the replica:

```
systemctl start pgbackrest-full.service
su - pgbackrest -c 'pgbackrest --config /etc/pgbackrest-server/pgbackrest.conf info'
```

Example:

```
stanza: main
    status: ok
    cipher: aes-256-cbc

    db (current)
        wal archive min/max (18): 000000010000000000000001/000000010000000000000007

        full backup: 20251227-083056F
            timestamp start/stop: 2025-12-27 08:30:56+01 / 2025-12-27 08:30:58+01
            wal start/stop: 000000010000000000000007 / 000000010000000000000007
            database size: 22.6MB, database backup size: 22.6MB
            repo1: backup set size: 2.9MB, backup size: 2.9MB
```

## Local Testing

The preferred way of locally testing the role is to use
[Podman](https://podman.io/) and
[molecule](https://docs.ansible.com/projects/molecule/).

List scenarios:

```
molecule list
```

Install dependencies:

```
molecule dependency [--scenario-name=default]
```

Run a single scenario:

```
molecule test [--scenario-name=default]
```

Run all scenarios:

```
molecule test --all
```
