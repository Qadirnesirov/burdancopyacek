HELP_1 = """✅**<u>Admin əmrləri:</u>**

**c** kanal oynatmağı nəzərdə tutur.

/pause or /cpause - Oynanan musiqini dayandırın.

/resume or /cresume- Dayandırılmış musiqini davam etdirin.

/mute or /cmute- Oynanan musiqinin səsini söndürün.

/unmute or /cunmute- Səssiz musiqinin səsini açın.


/skip or /cskip- Cari ifa olunan musiqini keçin.

/stop or /cstop- Musiqi çalmağı dayandırın.

/restart or /reload - Söhbətiniz üçün botu yenidən başladın """

HELP_2 = """✅<u>**Auth istifadəçiləri**</u>
Auth İstifadəçiləri söhbətinizdə admin hüquqları olmadan admin əmrlərindən istifadə edə bilərlər.

/auth [Username] - Qrupun AUTH LIST-ə istifadəçi əlavə edin.

/unauth [Username] - Qrupun AUTH LIST-dən istifadəçini silin.

/authusers - Qrupun AUTH SİYAHISINI yoxlayın."""

HELP_3 = """⚠️**<u>QARA SİYAHİ SAHİB FUNKSİYASI:</u>**

/blacklistchat [CHAT_ID] - Music Bot-dan istifadə etməklə istənilən söhbəti qara siyahıya salın

/whitelistchat [CHAT_ID] - Music Bot-dan istifadə edərək qara siyahıya salınmış söhbətləri ağ siyahıya daxil edin

/blacklistedchat - Bütün qara siyahıya alınmış söhbətləri yoxlayın.


👤**<u>BLOK OLUNMUŞ FUNKSİYA:</u>**

/block [İstifadəçi adı və ya istifadəçiyə cavab] - İstifadəçinin bot əmrlərindən istifadəsinin qarşısını alır.

/unblock [İstifadəçi adı və ya istifadəçiyə cavab] - İstifadəçini Botun Bloklanmış Siyahısından çıxarın.

/blockedusers - Bloklanmış İstifadəçi Siyahılarını yoxlayın
."""

HELP_4 = """🌐**<u>YAYIM FUNKSİYASI:</u>**
/broadcast [Mesaj və ya Mesaja Cavab] - Botun Xidmət edilən Çatlarına istənilən mesajı yayımlayın.

<u>yayım variantları:</u>

**-pin** : Bu, mesajınızı sabitləyəcək 

**-pinloud** : Bu, mesajınızı yüksək səsli bildirişlə bağlayacaq

**-user** : Bu, mesajınızı botunuzu işə salmış istifadəçilərə yayımlayacaq.

**-assistant** : Bu, mesajınızı botunuzun köməkçi hesabından yayımlayacaq.

**-nobot** : Bu, botunuzu mesaj yayımlamamağa məcbur edəcək

**Example:** `/broadcast -user -assistant -pin Salam Test`

"""
HELP_5 = """✅<u>**əlavə əmrlər:**</u>

/loop or /cloop [enable/disable] or [Aralarındakı nömrələr 1-10] 
    - Aktivləşdirildikdə, bot səsli söhbətdə cari ifa olunan musiqini 1-10 dəfə çevirir. Varsayılan olaraq 10 dəfə.

/language or /langs : İngilis dilini Bangla dilinə dəyişdirmək üçün

/shuffle or /cshuffle- Növbəyə qoyulmuş pleylistləri təsadüfi qarışdırır.

/google - Google ilə başqa bir şey axtarın

/image - Şəkil əldə edin

/ask - bir şey soruş 

/seek or /cseek - İrəli Musiqini öz müddətinizə qədər axtarın

/seekback or /cseekback - Geriyə Musiqini öz müddətinə qədər axtarın

/owner - bu repo yaradıcısının kim olduğunu yoxlayın

/donate - bot sahibi üçün ianə verin 🙂
/id or /info- İstifadəçi məlumatının yaradılması üçün bu cmd

/lyrics [Musiqi Adı] - İnternetdə xüsusi Musiqi üçün Lirikləri axtarır."""

HELP_6 = """✅**<u>Botun Server çalğı siyahıları:</u>**

/playlist  - Serverlərdə Saxlanmış Pleylistinizi Yoxlayın.

/deleteplaylist - Pleylistinizdə saxlanan hər hansı musiqini silin

/play  - Serverlərdən Saxlanmış Pleylistinizi oynatmağa başlayın."""

HELP_7 = """✨ **ping cmd :**

/ping- Botu pingləyin və Botun Ram, CPU və s. statistikasını yoxlayın.

/stats - Qlobal Statistikanın ən yaxşı 10 musiqisini əldə edin, botun ən yaxşı 10 istifadəçisi, botda ən yaxşı 10 söhbət, söhbətdə oynanan ən yaxşı 10 və s."""

HELP_8 = """✅<u>**oynatma Əmrləri:**</u>

Mövcud Əmrlər = play, vplay , cplay

ForcePlay Əmrləri = playforce , vplayforce , cplayforce

**c** kanal oynatmağı nəzərdə tutur.
**v** video oynatma deməkdir.
**force** güc oyunu üçün dayanır.

/play or /vplay or /cplay  - Bot verdiyiniz sorğunu səsli söhbətdə oynatmağa və ya səsli söhbətlərdə canlı bağlantıları yayımlamağa başlayacaq.

/playforce or /force or /vplayforce or /cplayforce -  **Məcbur Oyun** səsli söhbətdə cari ifa olunan treki dayandırır və növbəni pozmadan/təmizləmədən axtarılan treki dərhal ifa etməyə başlayır.

/channelplay [Söhbət istifadəçi adı və ya id] or [Disable] - Kanalı qrupa qoşun və qrupunuzdan kanalın səsli söhbətində musiqi yayımlayın."""

HELP_9 = """🔰**<u>SUDO İSTİFADƏÇİLƏRİNİ ƏLAVƏ EDİN və SİLİN:</u>**

/addsudo [İstifadəçi adı və ya istifadəçiyə cavab]

/delsudo [İstifadəçi adı və ya istifadəçiyə cavab]

🛃**<u>HEROKU:</u>**

/usage - Dyno İstifadəsi.

🌐**<u>CONFIG VARS:</u>**

/get_var - Heroku-dan konfiqurasiya var alın və ya .env.

/del_var - Heroku və ya hər hansı bir var silin .env.

/set_var [Var Name] [Value] - Heroku və ya .env-də Var təyin edin və ya Var-ı yeniləyin. Var və onun dəyərini boşluqla ayırın.


🤖**<u>BOT COMMANDS:</u>**

/reboot - Botunuzu yenidən başladın. 
/update - Botu yeniləyin.
/speedtest - Server sürətlərini yoxlayın
/maintenance [enable / disable] 
/logger [enable / disable] - Bot axtarış edilmiş sorğuları qeyd edən qrupda qeyd edir.
/get_log [Xətlərin sayı] - Heroku və ya vps-dən botunuzun qeydini əldə edin. Hər ikisi üçün işləyir.

⚡️**<u>PRIVATE BOT FUNCTION:</u>**
/authorize [CHAT_ID] - Botunuzdan istifadə etmək üçün söhbətə icazə verin.
/unauthorize [CHAT_ID] - Söhbətin botunuzdan istifadəsinə icazə verməyin.
/authorized - Botunuzun bütün icazə verilən söhbətlərini yoxlayın.
"""

HELP_10 = """🤑 **<u>Aktiv videoçatlar :</u>**

/activevoice - Botda aktiv səsli söhbətləri yoxlayın.
/activevideo - Botda aktiv video zəngləri yoxlayın.
/autoend [enable|disable] - Heç kim qulaq asmırsa, 3 dəqiqədən sonra avtomatik yayımın bitməsini aktiv edin."""

HELP_11 = """😅**<u> bot ilə başladı</u>**
/start : botu işə salın

/help : Əmrlərin təfərrüatlı izahatları ilə Əmrlər Köməkçisi Menyu əldə edin..

/reboot : söhbətiniz üçün botu yenidən başladın.

/settings - Daxili düymələrlə tam qrup parametrlərini əldə edin.

/sudolist - Sudo İstifadəçilərini yoxlayın ZatraMusicBot"""

HELP_12 = """👤**<u>GBAN FUNCTION:</u>**

/gban [İstifadəçi adı və ya istifadəçiyə cavab] - İstifadəçini botun xidmət etdiyi söhbətdən çəkin və onun botunuzdan istifadəsini dayandırın.

/ungban [İstifadəçi adı və ya istifadəçiyə cavab] - İstifadəçini Botun qadağan edilmiş Siyahısından çıxarın və ona botunuzdan istifadə etməyə icazə verin

/gbannedusers - Gbanned İstifadəçi Siyahılarını yoxlayın."""

HELP_13 = """👤**<u>TRUTH DARE FUNCTION:</u>**

/dareeng - Azərbaycanca idare edin

/darehin - Azərbaycan dilində cəsarət et 

/trutheng - Azərbaycan dilində həqiqəti qəbul edin.

/truthhin - Azərbaycan dilində həqiqəti qəbul edin."""
