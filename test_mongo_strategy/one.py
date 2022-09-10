host_strategy_content = {1: {'8203': {'curr_strategy_config_id': '26e28364bb9f40f58983fe2dc2c76f46', 'curr_timestamp': 1650354765.0,
                '00c5ad9aec534036849b0e825dba479d': {'base_object_type': 1, 'strategy_config_content': {
                    '_id': '00c5ad9aec534036849b0e825dba479d',
                    'configData': {'Name': 'com.ukui.panel.desktop', 'Path': '/',
                                   'Interfaces': 'com.ukui.panel.desktop', 'ukui-panel': {'blacklist': [{'entries': [
                            {'appname': 'org.gnome.Reversi', 'display_name_cn': 'org.gnome.Reversi',
                             'path': '/usr/share/applications/org.gnome.Reversi.desktop'}], 'pkgname': ''}],
                                                                                          'whitelist': [{'entries': [],
                                                                                                         'pkgname': ''}],
                                                                                          'mode': 'blacklist'}},
                    'hash': 'cde12f011378211521b3dc4e1abaa156',
                    'server_local': 'softwareRunControlPanel/00c5ad9aec534036849b0e825dba479d.json'}},
                '26e28364bb9f40f58983fe2dc2c76f46': {'base_object_type': 1, 'strategy_config_content': {
                    '_id': '26e28364bb9f40f58983fe2dc2c76f46',
                    'configData': {'Name': 'com.ukui.panel.desktop', 'Path': '/',
                                   'Interfaces': 'com.ukui.panel.desktop', 'ukui-panel': {'blacklist': [{'entries': [
                            {'appname': 'org.gnome.Reversi', 'display_name_cn': 'org.gnome.Reversi',
                             'path': '/usr/share/applications/org.gnome.Reversi.desktop'}], 'pkgname': ''}],
                                                                                          'whitelist': [{'entries': [],
                                                                                                         'pkgname': ''}],
                                                                                          'mode': 'blacklist'}},
                    'hash': 'cde12f011378211521b3dc4e1abaa156',
                    'server_local': 'softwareRunControlPanel/26e28364bb9f40f58983fe2dc2c76f46.json'}}}}}

mode_id_key = 1
config_type_key = "8203"
print(host_strategy_content[mode_id_key][config_type_key].pop('26e28364bb9f40f58983fe2dc2c76f46'))
print(host_strategy_content)


