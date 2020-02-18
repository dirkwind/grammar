# custom symmetric encryption
import random

keys = {
    0: '\'?IUû!wK░@ÚÏrþ¢9MÍ<ukZ:G¹Óà³á║ÈÁHïÎÔoËY┼J╠╬┴0i3²7X▓í└┤ªºv¶÷yð,µjça©* ø2▄êâ.úTpÂ’ÖØý█1ÆóÌ´╔╦[Õæb$Òä“·«åtÑã§ëßì6+;s╝g£B&Lé”▒═{EîmO°¿ü-¼¥┬èÊö5╚%Çh¾»¤q╗Þc½^×ôÐ4]"}=Ä¦(¯`▀│fD├ÛWÝS─zÀd╩Å¨Ã#ñNC┐QnÜù8/¦®ÙF­¸¡\\ÉAR)¬õÿxV|_■~òP>e±l╣',
    1: 'Ü×┼Úýæ]Z÷m±róz»¬╣êKú├wÉ³OªÇÍÛ╠╗ôÝ└BV1HdYg^Ó¶M­╬ï"vÁhX¨î>9¼┬¸ÿøÊxÄD│n´}(ET®kùIÒÆåÈûoÞc8áJsßÀí-ëqtÖ+Ð&”¦QØpÏã▀ò¥*G¯è©.05/²¿jLÂà¹$Ì§[)╚NWÙa¤Ã═3¢i°Î╝▄█Ñ{,\'`CÕ@Fä╦%A\\Ô¡éâ?b4Uõ;ð#¦!<╔’|S2Rö6_░:=~■┐uË║ì7µ þ¾╩«f┤£Å·üPñ─▓º┴e▒“y½çl',
    2: 'Õcç4Ñöa\';├G8h"[+Kó½¥Îàÿ1±>ÖÌ£7 SÙ¾qÏÝåñá’┐i²NB*x!v~í╚âIj┬/k|¨¢Ø·ïÅäÃrÂÆp{]┼P╠ÐÞþÓôs╣=ì5¶&æ▒n³êÚ█│:D“ÄßÔZ╦µXÛAC©0øõ.▄,Ç»uúë×└¹░Ò▓╗«RzJ?$╔û§E_yOT¤tW¦═%éQÍ´Mè┤Àm2@Ul¯L\\¼b¬dgH■îª╬#Ë°¸V`®”▀¡─ÊoF9)eã^}wº-ùòüðYf­╝Á6<║¿(ÜÈÉ¦÷╩┴3ý',
    3: '$╚┴})3╠ªgÚæ5"2a░óúeX¤│p▒’v┤Èy6ixSøÿç°Ò@ÔBEm*▓ï▄Î^=█²╬qu¦┐èl╦Ð¡ËÞ`R§oj¾&é7À¦-╗Í¹­º╣zQ íþîà~ZùwÁ>®ãA¿ÌÛ║{Ü4¬¸%N!ö/sL³nä├]µJÆÊ\\▀¥(dÙM¨KØÇ.\'áåCUìÃrÑ:ûô╩ð«ß┬Å©Ä£Ö┼8|âõVP±GkÉñëY“╝1Óý└╔;t<¼■T+”─Ï¶×Âò,W_êüÕ¯¢[9hI´Fcb÷·?»½fH#Ý0═DO',
    4: '┼ºCÊ¦êï?Àd¾]╩}csJØ│F▒Î▀3·á╗■iÉG# wû<«┴¥½ÒeÆÄ$*|”þ¼ýµ§!^’NÌa,óÂ÷h"ú¶├Xôb╝K┤ä╣Üì└DA­Å=ñVÞ(øÑPül9;ß©ÍI┬HM─~═0ÐÁ{¯5╔EL╦ð╠¢¨¹³QÚx-q®>ù&gRj27WÇæ“Õf╬t╚²▄¸4nBÝèÓÈéò×░»▓Umk¡\':YZõÖÏ¿Ù¤█£T´@1/åí%yªàpÔ¦v[_)¬┐ëÛu°±\\8║SçzoãO+`.â6îËÿÃör',
    5: '┼╦├ª/kËÑq7GÞæ1TÝ┴a´┤ê£┐.─Es╩ë¤ÛÇÉÓ9h)”M▒üâb└v█ÙÿñC~¿ZN³l▀Ö▄"OÁþÄ■╣o¬cD:»Ìº>d,¨P═iWASVû3║;ó¹j±©+╝ÐÅ®&¢LåúryÔ¼è5xØ“á{¸çù<õ╔¶Í=¾ÀY8▓Ã%┬·|Æ#öì6R Hà¦°^4Â¥g_¯2z\'0XµÒmôÎ«$IïF╚ä@ßUB([¡­-│píe½òt╗}Q÷\\wÜÈn╠ãJuÏ░`Õ×îÚ²?¦K!ý╬*ø]ðfé’§Ê',
    6: 'éöÈÀ╩z`j“@Z_ÉQ█Ì\\©þá&NêôG¸(®▄ã\'ð-§¬]╚fü¯æ°┐ûùu;K«╠»T#dú±PàYmº╬ÿ? ┴ÊÍ¶k┬Lò├ß╗õo:¹÷0£I╔.aqpí/S4,vËx²Øñ3w[▒ë▓║¿╦hE╣½¼▀Ã+µX·’}A7ÜD*8─C2s^FªÞ¥BMÓ"”Önì5Á<1çól┼´ÑÙRJåÄ└ÅrÏ¢)¦ÇÕ6by³Û░|Ôc│O┤HWâtUÝ=­ge¡¦╝¤!VÎèÚ$%{i~¾ýïÂÐ9×äÆÒ■î¨>ø═',
    7: '¤_bUÐhys½,Û©Lß\\;ÔGWÅà^▒xÂj`*▄a¯|£╣dÉ4÷¼Oå¦▀Í6õºnô┴ip3¸ä!?ÿw=ïX1ùgø®’\'+f■P│├µ╗Ä█╦└[ãÃ×┬╝]âqz”ö▓æîì╬ÇòëRT¬ ­È«Üá┐─ú°ý┤Ë#¶-²Ql0§:.{Ú%þé“9$ñI/ü·ð)¦¢"Þ¹BVF}»êrÏ³╠2Ø¨ÎmÑ║Nv╔╩~Z¥oóû>uC¿ÌçM¾Õ╚èÀÝ´<±(Á&JEKtckAíÒÊÖ═┼░@¡HÙDÆ7S5ªY8Óe',
    8: '©.Rë╗Ø8Ýâ1▓OÚø²"iÖ`F═læºÆv┬Þ(+─┼”)s“¥ÕZáÙE@õd0¬╚Ó½;╬2 ±Ô|7ßnVù*Ï«à{þÄ║└LaWÇûr¹╔<¿pSò¡É┤:eå®X³Û▒´ó§Ðm¦­u]_j×Ã¸µ╠»▄├D╦£éôIP╣zTí!6HÈ¢Â&’?[=■,öãN~BêÌbC3g\\$╩ï4ýy÷ä░c-^K┴▀│¤kèQ¯t·î\'Òðñü¼¾¨hÜÅç°fÊ┐Í}╝¶#UwÿÎÁì¦MÑúªJA59█x/YÀoq%ËG>',
    9: '¶{ae╔╚¦¦(Ï%ÇÅj#uW[À)Ö/¡Ìi¹pJõÒ"H║│Îwæ█A`5û<zcÓ7çßYM┤P├í¢´yÈÙò§½|èn×0Of▀êÜI▒Äà®v?ã¥­R┴·ÿ}rÚNþBböôØq┐hQ]²Ñ╬ñ╦KâS┼üÁ╗“*ù!▄~▓═’d¼8£Â└╩ú”@>23┬V_CËk-\\:ÍîóÞ&©TÊìð¬¸ÃXá¯¾¨µ6x─«Eg;.░$ª+╣ÆlsD^t╠¤³ZÉÕäÔý■é±Gø÷=°¿F9╝om,U º\'ÐëÝ»Lïå4Û1'
}

characters = list('!”’“"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ░▒▓│┤╣║╗╝┐└┴┬├─┼╚╔╩╦╠═╬█▄¦▀■')

def get_charset(alnum=False):
    '''copies the charaters varible'''
    if alnum:
        return [char for char in characters if char.isalnum()]
    return [char for char in characters] 

def generate_key(only_alnum=False):
    '''generates a key compatible with crunch'''
    result = r''
    charset = get_charset(only_alnum)
    for _ in range(0, len(charset)):
        result = result + str(charset.pop(charset.index(random.choice(charset))))
    return result

def crunch(phrase):
    '''Encrypts a string or decrypts a uncrunched string\n
    NOTE: any string that starts with a numeric character will automatically be decrypted rather that encrypted
    '''
    increment = 1
    result = ''

    try:
        # if key_num is at start of phrase
        alphabet = keys[int(phrase[0])]
        phrase = phrase[1:] # removes key_num from phrase
    except:
        # if there is no key_num at start of phrase
        key_num = random.randint(0, 9)
        alphabet = list(keys.get(key_num))
        result = str(key_num)

    for letter in phrase:
        index = alphabet.index(letter) + increment
        index = index % len(alphabet)
        result += alphabet[index]
        increment *= 2

    return result

def uncrunch(phrase):
    '''Encrypts a string or decrypts a uncrunched string\n
    NOTE: any string that starts with a numeric character will automatically be decrypted rather that encrypted
    '''
    result = ""
    increment = 1

    try:
        # if key_num is at start of phrase
        alphabet = keys[int(phrase[0])]
        phrase = phrase[1:] # removes key_num from 
    except:
        # if there is no key_num at start of phrase
        key_num = random.randint(0, 9)
        alphabet = keys.get(key_num)
        result = str(key_num) # result will start with keynum

    for letter in phrase:
        index = alphabet.index(letter) - increment
        index = index % len(alphabet)
        result += alphabet[index]
        increment *= 2

    return result

