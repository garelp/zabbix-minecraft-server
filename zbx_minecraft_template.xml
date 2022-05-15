<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
    <version>5.0</version>
    <date>2022-05-14T12:45:33Z</date>
    <groups>
        <group>
            <name>Templates</name>
        </group>
    </groups>
    <templates>
        <template>
            <template>Minecraft Stats Active</template>
            <name>Minecraft Stats Active</name>
            <description>Minecraft server status</description>
            <groups>
                <group>
                    <name>Templates</name>
                </group>
            </groups>
            <applications>
                <application>
                    <name>Minecraft</name>
                </application>
            </applications>	   
            <items>
                <item>
                    <name>Server Latency</name>
                    <key>minecraft.server.latency[{$MINECRAFT.SERVER.IP},{$MINECRAFT.SERVER.PORT}]</key>
                    <delay>120</delay>
                    <value_type>FLOAT</value_type>
                    <units>s</units>
                    <applications>
                        <application>
                            <name>Minecraft</name>
                        </application>
                    </applications>
                    <triggers>
                        <trigger>
                            <expression>last(/Minecraft Stats Active/minecraft.server.latency[{$MINECRAFT.SERVER.IP},{$MINECRAFT.SERVER.PORT}])=0</expression>
                            <name>Minecraft Server down</name>
                            <priority>HIGH</priority>
                        </trigger>
                    </triggers>
                </item>
                <item>
                    <name>Server connected users</name>
                    <key>minecraft.server.users[{$MINECRAFT.SERVER.IP},{$MINECRAFT.SERVER.PORT}]</key>
                    <delay>120</delay>
                    <applications>
                        <application>
                            <name>Minecraft</name>
                        </application>
                    </applications>
                </item>
            </items>
            <macros>
                <macro>
                    <macro>{$MINECRAFT.SERVER.IP}</macro>
                    <value>127.0.0.1</value>
                    <description>Ip or dns name for checks. If you have to change this, add this as a macro to your host.</description>
                </macro>
                <macro>
                    <macro>{$MINECRAFT.SERVER.PORT}</macro>
                    <value>25565</value>
                    <description>The port used for checks. If you have to change this, add this as a macro to your host.</description>
                </macro>
            </macros>
        </template>
    </templates>
    <graphs>
        <graph>
            <name>Connected Users</name>
            <graph_items>
                <graph_item>
                    <color>1A7C11</color>
                    <item>
                        <host>Minecraft Stats Active</host>
                        <key>minecraft.server.users[{$MINECRAFT.SERVER.IP},{$MINECRAFT.SERVER.PORT}]</key>
                    </item>
                </graph_item>
            </graph_items>
        </graph>
        <graph>
            <name>Server Latency</name>
            <graph_items>
                <graph_item>
                    <color>CCCCFF</color>
                    <item>
                        <host>Minecraft Stats Active</host>
                        <key>minecraft.server.latency[{$MINECRAFT.SERVER.IP},{$MINECRAFT.SERVER.PORT}]</key>
                    </item>
                </graph_item>
            </graph_items>
        </graph>
    </graphs>
</zabbix_export>
