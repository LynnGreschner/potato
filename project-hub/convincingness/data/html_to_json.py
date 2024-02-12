import json

html_code1 = """
<p><strong>Los geht's!</strong></p>
<p>Lesen Sie sich die folgende Aussage/Behauptung durch:</p>
<p><strong>Die Sonne erscheint aus dem Weltraum gesehen wei&szlig;.</strong></p>
<p>Lesen Sie sich jetzt die folgenden 4 Argumente f&uuml;r die Aussage sorgf&auml;ltig durch. Danach entscheiden Sie, welches der Argumente f&uuml;r Sie am &uuml;berzeugendsten wirkt.</p>
<p><span style="text-decoration: underline;">Argument 1:</span></p>
<p>Das Licht der Sonne ist grunds&auml;tzlich farblos, was an der Wellenl&auml;nge des emittierten Lichtes liegt. Auf der Erde nehmen wir Flammen und Feuer oft als gelbfarbig wahr, manchmal auch als blau oder farblos, abh&auml;ngig von der Temperatur der Flamme. Die extrem hei&szlig;e Flamme der Sonne brennt nach dieser Logik wei&szlig;. Dass die Sonne von der Erde aus gelb aussieht, liegt an der Atmosph&auml;re, die die Sonne ergibt. Diese ver&auml;ndert die Farbwahrnehmung durch eine Ver&auml;nderung der Wellenl&auml;nge des Lichtes - die w&uuml;rde wirkt auf uns gelblich bis gelb.</p>
<p><span style="text-decoration: underline;">Argument 2:</span></p>
<p>Wenn wir die Sonne von der Erde aus betrachten, erscheint Sie uns lediglich wei&szlig;, weil wir sie durch die Atmosph&auml;re betrachten. Gleiches Prinzip wie bei Wasser, das je nach Untergrund ein tief dunkles Blau annehmen kann, bis hin zu einem hellen T&uuml;rkis.</p>
<p><span style="text-decoration: underline;">Argument 3:</span></p>
<p>Betrachtet man die Sonne vom Weltraum aus, sieht sie wei&szlig; aus. Dass wir die Sonne hier gelb sehen, hat mit der Erdatmosph&auml;re zu tun. Die Lichtstrahlen verhalten sich im Weltraum jedoch anders, weshalb wir sie als wei&szlig; wahrnehmen.</p>
<p><span style="text-decoration: underline;">Argument 4:</span></p>
<p>die Sonne ist vom Weltraum aus gesehen wei&szlig;. sie erscheint nur bei uns auf der Erde als gelb oder orange. das hat etwas mit unserer Atmosph&auml;re zu tun die das Licht in gesto&szlig;en Ma&szlig;e braucht, die die Sonne f&uuml;r unsere Augen gelblich-orange erscheint.</p>
"""

html_code2 = """
<p><strong>Los geht's!</strong></p>
<p>Lesen Sie sich die folgende Aussage/Behauptung durch:</p>
<p><strong>Die Sonne erscheint aus dem Weltraum gesehen wei&szlig;.</strong></p>
<p>Lesen Sie sich jetzt die folgenden 4 Argumente f&uuml;r die Aussage sorgf&auml;ltig durch. Danach entscheiden Sie, welches der Argumente f&uuml;r Sie am &uuml;berzeugendsten wirkt.</p>
<p><span style="text-decoration: underline;">Argument 1:</span></p>
<p>Das Licht der Sonne ist grunds&auml;tzlich farblos, was an der Wellenl&auml;nge des emittierten Lichtes liegt. Auf der Erde nehmen wir Flammen und Feuer oft als gelbfarbig wahr, manchmal auch als blau oder farblos, abh&auml;ngig von der Temperatur der Flamme. Die extrem hei&szlig;e Flamme der Sonne brennt nach dieser Logik wei&szlig;. Dass die Sonne von der Erde aus gelb aussieht, liegt an der Atmosph&auml;re, die die Sonne ergibt. Diese ver&auml;ndert die Farbwahrnehmung durch eine Ver&auml;nderung der Wellenl&auml;nge des Lichtes - die w&uuml;rde wirkt auf uns gelblich bis gelb.</p>
<p><span style="text-decoration: underline;">Argument 2:</span></p>
<p>Wenn wir die Sonne von der Erde aus betrachten, erscheint Sie uns lediglich wei&szlig;, weil wir sie durch die Atmosph&auml;re betrachten. Gleiches Prinzip wie bei Wasser, das je nach Untergrund ein tief dunkles Blau annehmen kann, bis hin zu einem hellen T&uuml;rkis.</p>
<p><span style="text-decoration: underline;">Argument 3:</span></p>
<p>Betrachtet man die Sonne vom Weltraum aus, sieht sie wei&szlig; aus. Dass wir die Sonne hier gelb sehen, hat mit der Erdatmosph&auml;re zu tun. Die Lichtstrahlen verhalten sich im Weltraum jedoch anders, weshalb wir sie als wei&szlig; wahrnehmen.</p>
<p><span style="text-decoration: underline;">Argument 4:</span></p>
<p>die Sonne ist vom Weltraum aus gesehen wei&szlig;. sie erscheint nur bei uns auf der Erde als gelb oder orange. das hat etwas mit unserer Atmosph&auml;re zu tun die das Licht in gesto&szlig;en Ma&szlig;e braucht, die die Sonne f&uuml;r unsere Augen gelblich-orange erscheint.</p>
"""

html_code3 = """
<p><strong>Los geht's!</strong></p>
<p>Lesen Sie sich die folgende Aussage/Behauptung durch:</p>
<p><strong>Die Sonne erscheint aus dem Weltraum gesehen wei&szlig;.</strong></p>
<p>Lesen Sie sich jetzt die folgenden 4 Argumente f&uuml;r die Aussage sorgf&auml;ltig durch. Danach entscheiden Sie, welches der Argumente f&uuml;r Sie am &uuml;berzeugendsten wirkt.</p>
<p><span style="text-decoration: underline;">Argument 1:</span></p>
<p>Das Licht der Sonne ist grunds&auml;tzlich farblos, was an der Wellenl&auml;nge des emittierten Lichtes liegt. Auf der Erde nehmen wir Flammen und Feuer oft als gelbfarbig wahr, manchmal auch als blau oder farblos, abh&auml;ngig von der Temperatur der Flamme. Die extrem hei&szlig;e Flamme der Sonne brennt nach dieser Logik wei&szlig;. Dass die Sonne von der Erde aus gelb aussieht, liegt an der Atmosph&auml;re, die die Sonne ergibt. Diese ver&auml;ndert die Farbwahrnehmung durch eine Ver&auml;nderung der Wellenl&auml;nge des Lichtes - die w&uuml;rde wirkt auf uns gelblich bis gelb.</p>
<p><span style="text-decoration: underline;">Argument 2:</span></p>
<p>Wenn wir die Sonne von der Erde aus betrachten, erscheint Sie uns lediglich wei&szlig;, weil wir sie durch die Atmosph&auml;re betrachten. Gleiches Prinzip wie bei Wasser, das je nach Untergrund ein tief dunkles Blau annehmen kann, bis hin zu einem hellen T&uuml;rkis.</p>
<p><span style="text-decoration: underline;">Argument 3:</span></p>
<p>Betrachtet man die Sonne vom Weltraum aus, sieht sie wei&szlig; aus. Dass wir die Sonne hier gelb sehen, hat mit der Erdatmosph&auml;re zu tun. Die Lichtstrahlen verhalten sich im Weltraum jedoch anders, weshalb wir sie als wei&szlig; wahrnehmen.</p>
<p><span style="text-decoration: underline;">Argument 4:</span></p>
<p>die Sonne ist vom Weltraum aus gesehen wei&szlig;. sie erscheint nur bei uns auf der Erde als gelb oder orange. das hat etwas mit unserer Atmosph&auml;re zu tun die das Licht in gesto&szlig;en Ma&szlig;e braucht, die die Sonne f&uuml;r unsere Augen gelblich-orange erscheint.</p>
"""

data1 = {'id': '1', 'text': [html_code1]}
data2 = {'id': '2', 'text': [html_code2]}
data3 = {'id': '3', 'text': [html_code3]}

data_list = [data1, data2, data3]

with open('test_data_scheme.json', 'w') as f:
    json.dump(data_list, f, indent=4)

