# SCAP tailored controls from DISA STIG for RHEL6

## References

- <https://github.com/OpenSCAP/openscap>
- <https://github.com/ComplianceAsCode/content>

### HIGH impact tailored controls

#### Prevent Login to Accounts With Empty Password

- Rule ID: _xccdf_org.ssgproject.content_rule_no_empty_passwords_
- None

#### Disable Ctrl-Alt-Del Reboot Activation

- Rule ID: _xccdf_org.ssgproject.content_rule_disable_ctrlaltdel_reboot_
- None

#### Install Virus Scanning Software

- Rule ID: _xccdf_org.ssgproject.content_rule_install_antivirus_
- None

#### Verify and Correct File Permissions with RPM

- Rule ID: _xccdf_org.ssgproject.content_rule_rpm_verify_permissions_
- None

#### Verify and Correct Ownership with RPM

- Rule ID: _xccdf_org.ssgproject.content_rule_rpm_verify_ownership_
- None

### MEDIUM impact tailored controls

#### Ensure Logs Sent To Remote Host

- Rule ID: _xccdf_org.ssgproject.content_rule_rsyslog_remote_loghost_
- None

#### Ensure Logrotate Runs Periodically

- Rule ID: _xccdf_org.ssgproject.content_rule_ensure_logrotate_activated_
- None

#### Ensure System Log Files Have Correct Permissions

- Rule ID: _xccdf_org.ssgproject.content_rule_rsyslog_files_permissions_
- None

#### Install libreswan Package

- Rule ID: _xccdf_org.ssgproject.content_rule_package_libreswan_installed_
- None

#### Verify ip6tables Enabled if Using IPv6

- Rule ID: _xccdf_org.ssgproject.content_rule_service_ip6tables_enabled_
- None

#### Set Default ip6tables Policy for Incoming Packets

- Rule ID: _xccdf_org.ssgproject.content_rule_set_ip6tables_default_rule_
- None

#### Set Default iptables Policy for Forwarded Packets

- Rule ID: _xccdf_org.ssgproject.content_rule_set_iptables_default_rule_forward_
- None

#### Disable Bluetooth Kernel Module

- Rule ID: _xccdf_org.ssgproject.content_rule_kernel_module_bluetooth_disabled_
- None

#### Set Boot Loader Password in grub.conf

- Rule ID: _xccdf_org.ssgproject.content_rule_grub_legacy_password_
- None

#### Ensure Solid State Drives Do Not Contribute To Random-Number Entropy Pool

- Rule ID: _xccdf_org.ssgproject.content_rule_kernel_disable_entropy_contribution_for_solid_state_drives_
- None

#### Ensure that System Accounts Do Not Run a Shell Upon Login

- Rule ID: _xccdf_org.ssgproject.content_rule_no_shelllogin_for_systemaccounts_
- None

#### Set Password Minimum Length in login.defs

- Rule ID: _xccdf_org.ssgproject.content_rule_accounts_password_minlen_login_defs_
- None

#### Require Authentication for Single User Mode

- Rule ID: _xccdf_org.ssgproject.content_rule_require_singleuser_auth_
- None

#### Enable Smart Card Login

- Rule ID: _xccdf_org.ssgproject.content_rule_smartcard_auth_
- None

#### Set Interactive Session Timeout

- Rule ID: _xccdf_org.ssgproject.content_rule_accounts_tmout_
- None

#### Modify the System Login Banner

- Rule ID: _xccdf_org.ssgproject.content_rule_banner_etc_issue_
- None

#### Set Lockout Time for Failed Password Attempts

- Rule ID: _xccdf_org.ssgproject.content_rule_accounts_passwords_pam_faillock_unlock_time_
- None

#### Limit Password Reuse

- Rule ID: _xccdf_org.ssgproject.content_rule_accounts_password_pam_unix_remember_
- None

#### Set Interval For Counting Failed Password Attempts

- Rule ID: _xccdf_org.ssgproject.content_rule_accounts_passwords_pam_faillock_interval_
- None

#### Set Deny For Failed Password Attempts

- Rule ID: _xccdf_org.ssgproject.content_rule_accounts_passwords_pam_faillock_deny_
- None

#### Ensure All Files Are Owned by a Group

- Rule ID: _xccdf_org.ssgproject.content_rule_file_permissions_ungroupowned_
- None

#### Ensure All Files Are Owned by a User

- Rule ID: _xccdf_org.ssgproject.content_rule_no_files_unowned_by_user_
- None

#### Ensure All SUID Executables Are Authorized

- Rule ID: _xccdf_org.ssgproject.content_rule_file_permissions_unauthorized_suid_
- None

#### Verify that All World-Writable Directories Have Sticky Bits Set

- Rule ID: _xccdf_org.ssgproject.content_rule_dir_perms_world_writable_sticky_bits_
- None

#### Verify that System Executables Have Restrictive Permissions

- Rule ID: _xccdf_org.ssgproject.content_rule_file_permissions_binary_dirs_
- None

#### Verify that System Executables Have Root Ownership

- Rule ID: _xccdf_org.ssgproject.content_rule_file_ownership_binary_dirs_
- None

#### Verify that Shared Library Files Have Restrictive Permissions

- Rule ID: _xccdf_org.ssgproject.content_rule_file_permissions_library_dirs_
- None

#### Enable Randomized Layout of Virtual Address Space

- Rule ID: _xccdf_org.ssgproject.content_rule_sysctl_kernel_randomize_va_space_
- None

#### Add nosuid Option to /dev/shm

- Rule ID: _xccdf_org.ssgproject.content_rule_mount_option_dev_shm_nosuid_
- None

#### Add nodev Option to /dev/shm

- Rule ID: _xccdf_org.ssgproject.content_rule_mount_option_dev_shm_nodev_
- None

#### Add noexec Option to /dev/shm

- Rule ID: _xccdf_org.ssgproject.content_rule_mount_option_dev_shm_noexec_
- None

#### Disable Modprobe Loading of USB Storage Driver

- Rule ID: _xccdf_org.ssgproject.content_rule_kernel_module_usb-storage_disabled_
- None

#### Configure auditd Disk Full Action when Disk Space Is Full

- Rule ID: _xccdf_org.ssgproject.content_rule_auditd_data_disk_full_action_
- None

#### Configure auditd space_left on Low Disk Space

- Rule ID: _xccdf_org.ssgproject.content_rule_auditd_data_retention_space_left_
- None

#### Configure auditd admin_space_left Action on Low Disk Space

- Rule ID: _xccdf_org.ssgproject.content_rule_auditd_data_retention_admin_space_left_action_
- None

#### Configure auditd space_left Action on Low Disk Space

- Rule ID: _xccdf_org.ssgproject.content_rule_auditd_data_retention_space_left_action_
- None

#### Configure auditd Disk Error Action on Disk Error

- Rule ID: _xccdf_org.ssgproject.content_rule_auditd_data_disk_error_action_
- None

#### Ensure auditd Collects Unauthorized Access Attempts to Files (unsuccessful)

- Rule ID: _xccdf_org.ssgproject.content_rule_audit_rules_unsuccessful_file_modification_
- None

#### Ensure auditd Collects File Deletion Events by User

- Rule ID: _xccdf_org.ssgproject.content_rule_audit_rules_file_deletion_events_
- None

#### Ensure auditd Collects Information on the Use of Privileged Commands

- Rule ID: _xccdf_org.ssgproject.content_rule_audit_rules_privileged_commands_
- None

#### Configure SNMP Service to Use Only SNMPv3 or Newer

- Rule ID: _xccdf_org.ssgproject.content_rule_snmpd_use_newer_protocol_
- None

#### Disable Automatic Bug Reporting Tool (abrtd)

- Rule ID: _xccdf_org.ssgproject.content_rule_service_abrtd_disabled_
- None

#### Set SSH Client Alive Max Count

- Rule ID: _xccdf_org.ssgproject.content_rule_sshd_set_keepalive_
- None

### LOW impact tailored controls

#### Limit the Number of Concurrent Login Sessions Allowed Per User

- Rule ID: _xccdf_org.ssgproject.content_rule_accounts_max_concurrent_login_sessions_
- None

#### Ensure PAM Displays Last Logon/Access Notification

- Rule ID: _xccdf_org.ssgproject.content_rule_display_login_attempts_
- None

#### Uninstall openldap-servers Package

- Rule ID: _xccdf_org.ssgproject.content_rule_package_openldap-servers_removed_
- None

#### Disable Red Hat Network Service (rhnsd)

- Rule ID: _xccdf_org.ssgproject.content_rule_service_rhnsd_disabled_
- None

### UNKNOWN impact tailored controls

#### Ensure the Default Bash Umask is Set Correctly

- Rule ID: _xccdf_org.ssgproject.content_rule_accounts_umask_etc_bashrc_
- None

#### Ensure the Default C Shell Umask is Set Correctly

- Rule ID: _xccdf_org.ssgproject.content_rule_accounts_umask_etc_csh_cshrc_
- None

#### Ensure the Default Umask is Set Correctly in /etc/profile

- Rule ID: _xccdf_org.ssgproject.content_rule_accounts_umask_etc_profile_
- None

#### Set Daemon Umask

- Rule ID: _xccdf_org.ssgproject.content_rule_umask_for_daemons_
- None

#### Require Client SMB Packet Signing, if using mount.cifs

- Rule ID: _xccdf_org.ssgproject.content_rule_mount_option_smb_client_signing_
- None

#### Disable DHCP Client in ifcfg

- Rule ID: _xccdf_org.ssgproject.content_rule_sysconfig_networking_bootproto_ifcfg_
- None

