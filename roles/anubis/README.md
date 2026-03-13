# Ansible Role Anubis

Install and configure [Anubis](https://anubis.techaro.lol), a Web AI Firewall Utility.

<!-- ANSIBLE DOCSMITH TOC START -->
* [Role variables](#variables)
  * [`anubis_version`](#variable-anubis_version)
  * [`anubis_arch`](#variable-anubis_arch)
  * [`anubis_deb`](#variable-anubis_deb)
  * [`anubis_bot_policies`](#variable-anubis_bot_policies)
  * [`anubis_asset_lookup_header`](#variable-anubis_asset_lookup_header)
  * [`anubis_base_prefix`](#variable-anubis_base_prefix)
  * [`anubis_bind`](#variable-anubis_bind)
  * [`anubis_bind_network`](#variable-anubis_bind_network)
  * [`anubis_challenge_title`](#variable-anubis_challenge_title)
  * [`anubis_cookie_domain`](#variable-anubis_cookie_domain)
  * [`anubis_cookie_dynamic_domain`](#variable-anubis_cookie_dynamic_domain)
  * [`anubis_cookie_expiration_time`](#variable-anubis_cookie_expiration_time)
  * [`anubis_custom_real_ip_header`](#variable-anubis_custom_real_ip_header)
  * [`anubis_cookie_partitioned`](#variable-anubis_cookie_partitioned)
  * [`anubis_cookie_prefix`](#variable-anubis_cookie_prefix)
  * [`anubis_cookie_secure`](#variable-anubis_cookie_secure)
  * [`anubis_cookie_same_site`](#variable-anubis_cookie_same_site)
  * [`anubis_difficulty`](#variable-anubis_difficulty)
  * [`anubis_difficulty_in_jwt`](#variable-anubis_difficulty_in_jwt)
  * [`anubis_ed25519_private_key_hex`](#variable-anubis_ed25519_private_key_hex)
  * [`anubis_ed25519_private_key_hex_file`](#variable-anubis_ed25519_private_key_hex_file)
  * [`anubis_error_title`](#variable-anubis_error_title)
  * [`anubis_jwt_restriction_header`](#variable-anubis_jwt_restriction_header)
  * [`anubis_metrics_bind`](#variable-anubis_metrics_bind)
  * [`anubis_metrics_bind_network`](#variable-anubis_metrics_bind_network)
  * [`anubis_og_expiry_time`](#variable-anubis_og_expiry_time)
  * [`anubis_og_passthrough`](#variable-anubis_og_passthrough)
  * [`anubis_og_cache_consider_host`](#variable-anubis_og_cache_consider_host)
  * [`anubis_overlay_folder`](#variable-anubis_overlay_folder)
  * [`anubis_policy_fname`](#variable-anubis_policy_fname)
  * [`anubis_public_url`](#variable-anubis_public_url)
  * [`anubis_redirect_domains`](#variable-anubis_redirect_domains)
  * [`anubis_serve_robots_txt`](#variable-anubis_serve_robots_txt)
  * [`anubis_slog_level`](#variable-anubis_slog_level)
  * [`anubis_socket_mode`](#variable-anubis_socket_mode)
  * [`anubis_strip_base_prefix`](#variable-anubis_strip_base_prefix)
  * [`anubis_target`](#variable-anubis_target)
  * [`anubis_use_remote_address`](#variable-anubis_use_remote_address)
  * [`anubis_use_simplified_explanation`](#variable-anubis_use_simplified_explanation)
  * [`anubis_use_templates`](#variable-anubis_use_templates)
  * [`anubis_webmaster_email`](#variable-anubis_webmaster_email)
  * [`anubis_xff_strip_private`](#variable-anubis_xff_strip_private)
  * [`anubis_forced_language`](#variable-anubis_forced_language)
  * [`anubis_hs512_secret`](#variable-anubis_hs512_secret)
  * [`anubis_target_disable_keepalive`](#variable-anubis_target_disable_keepalive)
  * [`anubis_target_host`](#variable-anubis_target_host)
  * [`anubis_target_insecure_skip_verify`](#variable-anubis_target_insecure_skip_verify)
  * [`anubis_target_sni`](#variable-anubis_target_sni)
  * [`anubis_bbolt_path`](#variable-anubis_bbolt_path)
  * [`anubis_valkey_url`](#variable-anubis_valkey_url)
<!-- ANSIBLE DOCSMITH TOC END -->
<!-- ANSIBLE DOCSMITH MAIN START -->

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description (abstract) |
|----------|------|----------|---------|------------------------|
| `anubis_version` | `str` | No | `"1.25.0"` | Version of the binary.<br><br>See L(releases,https://github.com/TecharoHQ/anubis/releases). |
| `anubis_arch` | `str` | No | `"amd64"` | Architecture of the system to install Anubis. |
| `anubis_deb` | `str` | No | `"https://github.com/TecharoHQ/anubis/releases/download/ v{{ anubis_version }}/anubis_{{ anubis_version }}_{{ anubis_arch }}.deb"` | URL of the debian package to install. |
| `anubis_bot_policies` | `dict` | No | `{}` | Configure bot policies.<br><br>See L(Policy Definitions,https://anubis.techaro.lol/docs/admin/policies). |
| `anubis_asset_lookup_header` | `str` | No | N/A | Define the C(ASSET_LOOKUP_HEADER) environment variable. |
| `anubis_base_prefix` | `str` | No | N/A | Define the C(BASE_PREFIX) environment variable. |
| `anubis_bind` | `str` | No | `":8923"` | Define the C(BIND) environment variable. |
| `anubis_bind_network` | `str` | No | N/A | Define the C(BIND_NETWORK) environment variable. |
| `anubis_challenge_title` | `str` | No | N/A | Define the C(CHALLENGE_TITLE) environment variable. |
| `anubis_cookie_domain` | `str` | No | N/A | Define the C(COOKIE_DOMAIN) environment variable. |
| `anubis_cookie_dynamic_domain` | `bool` | No | N/A | Define the C(COOKIE_DYNAMIC_DOMAIN) environment variable. |
| `anubis_cookie_expiration_time` | `str` | No | N/A | Define the C(COOKIE_EXPIRATION_TIME) environment variable. |
| `anubis_custom_real_ip_header` | `str` | No | N/A | Define the C(CUSTOM_REAL_IP_HEADER) environment variable. |
| `anubis_cookie_partitioned` | `bool` | No | N/A | Define the C(COOKIE_PARTITIONED) environment variable. |
| `anubis_cookie_prefix` | `str` | No | N/A | Define the C(COOKIE_PREFIX) environment variable. |
| `anubis_cookie_secure` | `bool` | No | N/A | Define the C(COOKIE_SECURE) environment variable. |
| `anubis_cookie_same_site` | `str` | No | N/A | Define the C(COOKIE_SAME_SITE) environment variable. |
| `anubis_difficulty` | `int` | No | `4` | Define the C(DIFFICULTY) environment variable. |
| `anubis_difficulty_in_jwt` | `bool` | No | N/A | Define the C(DIFFICULTY_IN_JWT) environment variable. |
| `anubis_ed25519_private_key_hex` | `str` | No | N/A | Define the C(ED25519_PRIVATE_KEY_HEX) environment variable. |
| `anubis_ed25519_private_key_hex_file` | `str` | No | N/A | Define the C(ED25519_PRIVATE_KEY_HEX_FILE) environment variable. |
| `anubis_error_title` | `str` | No | N/A | Define the C(ERROR_TITLE) environment variable. |
| `anubis_jwt_restriction_header` | `str` | No | N/A | Define the C(JWT_RESTRICTION_HEADER) environment variable. |
| `anubis_metrics_bind` | `str` | No | `":9090"` | Define the C(METRICS_BIND) environment variable. |
| `anubis_metrics_bind_network` | `str` | No | N/A | Define the C(METRICS_BIND_NETWORK) environment variable. |
| `anubis_og_expiry_time` | `str` | No | N/A | Define the C(OG_EXPIRY_TIME) environment variable. |
| `anubis_og_passthrough` | `bool` | No | N/A | Define the C(OG_PASSTHROUGH) environment variable. |
| `anubis_og_cache_consider_host` | `bool` | No | N/A | Define the C(OG_CACHE_CONSIDER_HOST) environment variable. |
| `anubis_overlay_folder` | `str` | No | N/A | Define the C(OVERLAY_FOLDER) environment variable. |
| `anubis_policy_fname` | `path` | No | `"/etc/anubis/default.botPolicies.yaml"` | Define the C(POLICY_FNAME) environment variable. |
| `anubis_public_url` | `str` | No | N/A | Define the C(PUBLIC_URL) environment variable. |
| `anubis_redirect_domains` | `list` | No | N/A | Define the C(REDIRECT_DOMAINS) environment variable.<br><br>Expect a list of domains that will be transformed to a coma separated list. |
| `anubis_serve_robots_txt` | `bool` | No | N/A | Define the C(SERVE_ROBOTS_TXT) environment variable. |
| `anubis_slog_level` | `str` | No | N/A | Define the C(SLOG_LEVEL) environment variable. |
| `anubis_socket_mode` | `str` | No | N/A | Define the C(SOCKET_MODE) environment variable. |
| `anubis_strip_base_prefix` | `bool` | No | N/A | Define the C(STRIP_BASE_PREFIX) environment variable. |
| `anubis_target` | `str` | No | `"http://localhost:3923"` | Define the C(TARGET) environment variable. |
| `anubis_use_remote_address` | `str` | No | N/A | Define the C(USE_REMOTE_ADDRESS) environment variable. |
| `anubis_use_simplified_explanation` | `bool` | No | N/A | Define the C(USE_SIMPLIFIED_EXPLANATION) environment variable. |
| `anubis_use_templates` | `bool` | No | N/A | Define the C(USE_TEMPLATES) environment variable. |
| `anubis_webmaster_email` | `str` | No | N/A | Define the C(WEBMASTER_EMAIL) environment variable. |
| `anubis_xff_strip_private` | `bool` | No | N/A | Define the C(XFF_STRIP_PRIVATE) environment variable. |
| `anubis_forced_language` | `str` | No | N/A | Define the C(FORCED_LANGUAGE) environment variable. |
| `anubis_hs512_secret` | `str` | No | N/A | Define the C(HS512_SECRET) environment variable. |
| `anubis_target_disable_keepalive` | `bool` | No | N/A | Define the C(TARGET_DISABLE_KEEPALIVE) environment variable. |
| `anubis_target_host` | `str` | No | N/A | Define the C(TARGET_HOST) environment variable. |
| `anubis_target_insecure_skip_verify` | `bool` | No | N/A | Define the C(TARGET_INSECURE_SKIP_VERIFY) environment variable. |
| `anubis_target_sni` | `str` | No | N/A | Define the C(TARGET_SNI) environment variable. |
| `anubis_bbolt_path` | `path` | No | N/A | Path to the BBolt store backend. |
| `anubis_valkey_url` | `str` | No | N/A | URL of the Valkey store backend. |

### `anubis_version`<a id="variable-anubis_version"></a>

[*⇑ Back to ToC ⇑*](#toc)

Version of the binary.

See L(releases,https://github.com/TecharoHQ/anubis/releases).

- **Type**: `str`
- **Required**: No
- **Default**: `"1.25.0"`



### `anubis_arch`<a id="variable-anubis_arch"></a>

[*⇑ Back to ToC ⇑*](#toc)

Architecture of the system to install Anubis.

- **Type**: `str`
- **Required**: No
- **Default**: `"amd64"`



### `anubis_deb`<a id="variable-anubis_deb"></a>

[*⇑ Back to ToC ⇑*](#toc)

URL of the debian package to install.

- **Type**: `str`
- **Required**: No
- **Default**: `"https://github.com/TecharoHQ/anubis/releases/download/ v{{ anubis_version }}/anubis_{{ anubis_version }}_{{ anubis_arch }}.deb"`



### `anubis_bot_policies`<a id="variable-anubis_bot_policies"></a>

[*⇑ Back to ToC ⇑*](#toc)

Configure bot policies.

See L(Policy Definitions,https://anubis.techaro.lol/docs/admin/policies).

- **Type**: `dict`
- **Required**: No
- **Default**: `{}`



### `anubis_asset_lookup_header`<a id="variable-anubis_asset_lookup_header"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(ASSET_LOOKUP_HEADER) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_base_prefix`<a id="variable-anubis_base_prefix"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(BASE_PREFIX) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_bind`<a id="variable-anubis_bind"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(BIND) environment variable.

- **Type**: `str`
- **Required**: No
- **Default**: `":8923"`



### `anubis_bind_network`<a id="variable-anubis_bind_network"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(BIND_NETWORK) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_challenge_title`<a id="variable-anubis_challenge_title"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(CHALLENGE_TITLE) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_cookie_domain`<a id="variable-anubis_cookie_domain"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(COOKIE_DOMAIN) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_cookie_dynamic_domain`<a id="variable-anubis_cookie_dynamic_domain"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(COOKIE_DYNAMIC_DOMAIN) environment variable.

- **Type**: `bool`
- **Required**: No



### `anubis_cookie_expiration_time`<a id="variable-anubis_cookie_expiration_time"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(COOKIE_EXPIRATION_TIME) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_custom_real_ip_header`<a id="variable-anubis_custom_real_ip_header"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(CUSTOM_REAL_IP_HEADER) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_cookie_partitioned`<a id="variable-anubis_cookie_partitioned"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(COOKIE_PARTITIONED) environment variable.

- **Type**: `bool`
- **Required**: No



### `anubis_cookie_prefix`<a id="variable-anubis_cookie_prefix"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(COOKIE_PREFIX) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_cookie_secure`<a id="variable-anubis_cookie_secure"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(COOKIE_SECURE) environment variable.

- **Type**: `bool`
- **Required**: No



### `anubis_cookie_same_site`<a id="variable-anubis_cookie_same_site"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(COOKIE_SAME_SITE) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_difficulty`<a id="variable-anubis_difficulty"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(DIFFICULTY) environment variable.

- **Type**: `int`
- **Required**: No
- **Default**: `4`



### `anubis_difficulty_in_jwt`<a id="variable-anubis_difficulty_in_jwt"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(DIFFICULTY_IN_JWT) environment variable.

- **Type**: `bool`
- **Required**: No



### `anubis_ed25519_private_key_hex`<a id="variable-anubis_ed25519_private_key_hex"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(ED25519_PRIVATE_KEY_HEX) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_ed25519_private_key_hex_file`<a id="variable-anubis_ed25519_private_key_hex_file"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(ED25519_PRIVATE_KEY_HEX_FILE) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_error_title`<a id="variable-anubis_error_title"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(ERROR_TITLE) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_jwt_restriction_header`<a id="variable-anubis_jwt_restriction_header"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(JWT_RESTRICTION_HEADER) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_metrics_bind`<a id="variable-anubis_metrics_bind"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(METRICS_BIND) environment variable.

- **Type**: `str`
- **Required**: No
- **Default**: `":9090"`



### `anubis_metrics_bind_network`<a id="variable-anubis_metrics_bind_network"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(METRICS_BIND_NETWORK) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_og_expiry_time`<a id="variable-anubis_og_expiry_time"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(OG_EXPIRY_TIME) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_og_passthrough`<a id="variable-anubis_og_passthrough"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(OG_PASSTHROUGH) environment variable.

- **Type**: `bool`
- **Required**: No



### `anubis_og_cache_consider_host`<a id="variable-anubis_og_cache_consider_host"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(OG_CACHE_CONSIDER_HOST) environment variable.

- **Type**: `bool`
- **Required**: No



### `anubis_overlay_folder`<a id="variable-anubis_overlay_folder"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(OVERLAY_FOLDER) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_policy_fname`<a id="variable-anubis_policy_fname"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(POLICY_FNAME) environment variable.

- **Type**: `path`
- **Required**: No
- **Default**: `"/etc/anubis/default.botPolicies.yaml"`



### `anubis_public_url`<a id="variable-anubis_public_url"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(PUBLIC_URL) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_redirect_domains`<a id="variable-anubis_redirect_domains"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(REDIRECT_DOMAINS) environment variable.

Expect a list of domains that will be transformed to a coma separated list.

- **Type**: `list`
- **Required**: No



### `anubis_serve_robots_txt`<a id="variable-anubis_serve_robots_txt"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(SERVE_ROBOTS_TXT) environment variable.

- **Type**: `bool`
- **Required**: No



### `anubis_slog_level`<a id="variable-anubis_slog_level"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(SLOG_LEVEL) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_socket_mode`<a id="variable-anubis_socket_mode"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(SOCKET_MODE) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_strip_base_prefix`<a id="variable-anubis_strip_base_prefix"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(STRIP_BASE_PREFIX) environment variable.

- **Type**: `bool`
- **Required**: No



### `anubis_target`<a id="variable-anubis_target"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(TARGET) environment variable.

- **Type**: `str`
- **Required**: No
- **Default**: `"http://localhost:3923"`



### `anubis_use_remote_address`<a id="variable-anubis_use_remote_address"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(USE_REMOTE_ADDRESS) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_use_simplified_explanation`<a id="variable-anubis_use_simplified_explanation"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(USE_SIMPLIFIED_EXPLANATION) environment variable.

- **Type**: `bool`
- **Required**: No



### `anubis_use_templates`<a id="variable-anubis_use_templates"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(USE_TEMPLATES) environment variable.

- **Type**: `bool`
- **Required**: No



### `anubis_webmaster_email`<a id="variable-anubis_webmaster_email"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(WEBMASTER_EMAIL) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_xff_strip_private`<a id="variable-anubis_xff_strip_private"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(XFF_STRIP_PRIVATE) environment variable.

- **Type**: `bool`
- **Required**: No



### `anubis_forced_language`<a id="variable-anubis_forced_language"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(FORCED_LANGUAGE) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_hs512_secret`<a id="variable-anubis_hs512_secret"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(HS512_SECRET) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_target_disable_keepalive`<a id="variable-anubis_target_disable_keepalive"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(TARGET_DISABLE_KEEPALIVE) environment variable.

- **Type**: `bool`
- **Required**: No



### `anubis_target_host`<a id="variable-anubis_target_host"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(TARGET_HOST) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_target_insecure_skip_verify`<a id="variable-anubis_target_insecure_skip_verify"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(TARGET_INSECURE_SKIP_VERIFY) environment variable.

- **Type**: `bool`
- **Required**: No



### `anubis_target_sni`<a id="variable-anubis_target_sni"></a>

[*⇑ Back to ToC ⇑*](#toc)

Define the C(TARGET_SNI) environment variable.

- **Type**: `str`
- **Required**: No



### `anubis_bbolt_path`<a id="variable-anubis_bbolt_path"></a>

[*⇑ Back to ToC ⇑*](#toc)

Path to the BBolt store backend.

- **Type**: `path`
- **Required**: No



### `anubis_valkey_url`<a id="variable-anubis_valkey_url"></a>

[*⇑ Back to ToC ⇑*](#toc)

URL of the Valkey store backend.

- **Type**: `str`
- **Required**: No




<!-- ANSIBLE DOCSMITH MAIN END -->

## Example

```yaml
- hosts: all
  roles:
    - hachyderm.general.anubis
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
