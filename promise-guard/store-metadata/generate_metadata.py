#!/usr/bin/env python3
"""Build Promise Guard App Store and Google Play metadata from reviewed locale copy."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

PRIVACY_URL = "https://lrodeveloperr.github.io/privacy-policy/promise-guard/privacy/"
SUPPORT_URL = "https://lrodeveloperr.github.io/privacy-policy/promise-guard/support/"
MARKETING_URL = "https://lrodeveloperr.github.io/privacy-policy/promise-guard/"


def p(subtitle, promo, short, keywords, intro, features, private, ios, android, caution):
    return {
        "subtitle": subtitle,
        "promo": promo,
        "short": short,
        "keywords": keywords,
        "intro": intro,
        "features": features,
        "private": private,
        "ios": ios,
        "android": android,
        "caution": caution,
    }


PACKS = {
    "en": p(
        "Keep provider promises clear",
        "Capture what was promised, add dates and supporting items, track what happened and prepare a factual personal summary—without an account or ads.",
        "Record provider promises, dates and outcomes—locally, with no account or ads.",
        "record,reminder,report,refund,provider,follow-up,commitment",
        "What was promised should not disappear into memory. Promise Guard gives you a calm, structured place to record a provider's promise and what happens next.",
        ["Capture the provider, exact promise, source, dates, amount and reference", "Keep the original entry and add timestamped corrections, updates and outcomes", "Attach supporting files and set private reminders", "See open, due, resolved and archived records at a glance", "Prepare a one-page factual personal summary and review it before sharing"],
        "Local-first by design: no GoodUse Studios account or record-content server is required. No ads. You choose if and where to export, back up or share.",
        "Create two complete records at no charge. A one-time in-app purchase unlocks creation of additional records. Existing records remain usable without the unlock.",
        "Create two complete records at no charge. Creating additional records requires an auto-renewing monthly subscription. Existing records remain usable if the subscription ends.",
        "Promise Guard does not verify entries, decide whether a promise was breached or provide legal advice. Reports are personal summaries built from your entries.",
    ),
    "es": p(
        "Tus promesas, bien claras",
        "Registra lo prometido, añade fechas y documentos, sigue el resultado y prepara un resumen personal objetivo. Sin cuenta y sin anuncios.",
        "Registra promesas, fechas y resultados sin cuenta ni anuncios.",
        "promesa,registro,recordatorio,informe,reembolso,empresa",
        "Lo que una empresa prometió no debería depender de la memoria. Promise Guard te ofrece un espacio ordenado para registrar la promesa y lo que ocurre después.",
        ["Anota la empresa, las palabras exactas, el canal, las fechas, el importe y la referencia", "Conserva la entrada original y añade correcciones, novedades y resultados con fecha", "Adjunta archivos de apoyo y programa recordatorios privados", "Consulta de un vistazo los registros abiertos, pendientes, resueltos y archivados", "Prepara un resumen personal de una página y revísalo antes de compartirlo"],
        "Diseño local: no necesitas una cuenta ni un servidor de GoodUse Studios para guardar el contenido. Sin anuncios. Tú decides si exportas, respaldas o compartes.",
        "Crea dos registros completos sin coste. Una compra única dentro de la app permite crear más. Los registros existentes siguen disponibles sin la compra.",
        "Crea dos registros completos sin coste. Para crear más necesitas una suscripción mensual con renovación automática. Los registros existentes siguen disponibles si termina la suscripción.",
        "Promise Guard no verifica las entradas, no decide si hubo incumplimiento ni ofrece asesoramiento jurídico. Los informes son resúmenes personales basados en tus datos.",
    ),
    "pt": p(
        "Promessas sempre bem claras",
        "Registe o que foi prometido, junte datas e ficheiros, acompanhe o resultado e prepare um resumo factual. Sem conta e sem anúncios.",
        "Registe promessas, datas e resultados localmente, sem conta nem anúncios.",
        "promessa,registo,lembrete,relatório,reembolso,empresa",
        "O que uma empresa prometeu não deve ficar dependente da memória. O Promise Guard oferece um espaço organizado para registar a promessa e o que acontece depois.",
        ["Registe a empresa, as palavras exatas, o canal, as datas, o valor e a referência", "Mantenha a entrada original e acrescente correções, atualizações e resultados datados", "Junte ficheiros de apoio e defina lembretes privados", "Veja de imediato registos abertos, pendentes, resolvidos e arquivados", "Prepare um resumo pessoal factual de uma página e reveja-o antes de partilhar"],
        "Concebido para armazenamento local: não é necessária uma conta nem um servidor de conteúdos da GoodUse Studios. Sem anúncios. É o utilizador que decide se exporta, faz cópia ou partilha.",
        "Crie dois registos completos sem custo. Uma compra única na aplicação desbloqueia a criação de mais registos. Os registos existentes continuam acessíveis sem a compra.",
        "Crie dois registos completos sem custo. Para criar mais, é necessária uma subscrição mensal com renovação automática. Os registos existentes continuam acessíveis se a subscrição terminar.",
        "O Promise Guard não verifica entradas, não decide se houve incumprimento e não presta aconselhamento jurídico. Os relatórios são resumos pessoais criados a partir dos seus dados.",
    ),
    "fr": p(
        "Gardez les promesses au clair",
        "Consignez la promesse, ajoutez dates et pièces, suivez le résultat et préparez un résumé personnel factuel. Sans compte ni publicité.",
        "Consignez promesses, dates et résultats, sans compte ni publicité.",
        "promesse,suivi,rappel,rapport,remboursement,prestataire",
        "Une promesse faite par un prestataire ne devrait pas dépendre de votre mémoire. Promise Guard vous offre un espace calme et structuré pour la consigner et suivre la suite.",
        ["Notez le prestataire, les termes exacts, le canal, les dates, le montant et la référence", "Conservez l'entrée d'origine et ajoutez des corrections, mises à jour et résultats horodatés", "Ajoutez des pièces d'appui et programmez des rappels privés", "Repérez les dossiers ouverts, à échéance, résolus et archivés", "Préparez un résumé personnel factuel d'une page et vérifiez-le avant partage"],
        "Conçu pour un stockage local : aucun compte ni serveur de contenu GoodUse Studios n'est requis. Sans publicité. Vous choisissez si vous exportez, sauvegardez ou partagez.",
        "Créez deux dossiers complets sans frais. Un achat intégré unique permet d'en créer davantage. Vos dossiers existants restent accessibles sans cet achat.",
        "Créez deux dossiers complets sans frais. Une souscription mensuelle à renouvellement automatique est requise pour en créer davantage. Vos dossiers existants restent accessibles après la fin de la souscription.",
        "Promise Guard ne vérifie pas les saisies, ne conclut pas à une violation et ne fournit pas de conseil juridique. Les rapports sont des résumés personnels issus de vos données.",
    ),
    "de": p(
        "Zusagen klar dokumentieren",
        "Halten Sie Zusagen, Termine und Unterlagen fest, verfolgen Sie den Verlauf und erstellen Sie eine sachliche Übersicht – ohne Konto und Werbung.",
        "Zusagen, Termine und Ergebnisse lokal festhalten – ohne Konto oder Werbung.",
        "Zusage,Notiz,Erinnerung,Bericht,Erstattung,Anbieter",
        "Eine Zusage eines Anbieters sollte nicht nur vom Gedächtnis abhängen. Promise Guard bietet einen ruhigen, strukturierten Ort für die Zusage und den weiteren Verlauf.",
        ["Anbieter, genauen Wortlaut, Kanal, Termine, Betrag und Referenz erfassen", "Originaleintrag erhalten und datierte Korrekturen, Aktualisierungen und Ergebnisse ergänzen", "Unterstützende Dateien hinzufügen und private Erinnerungen festlegen", "Offene, fällige, erledigte und archivierte Einträge überblicken", "Sachliche persönliche Ein-Seiten-Übersicht vor dem Teilen prüfen"],
        "Lokal ausgerichtet: Für die Inhalte ist weder ein GoodUse-Studios-Konto noch ein Inhaltsserver erforderlich. Keine Werbung. Sie bestimmen über Export, Sicherung und Freigabe.",
        "Zwei vollständige Einträge können kostenlos erstellt werden. Ein einmaliger In-App-Kauf schaltet weitere Einträge frei. Bestehende Einträge bleiben auch ohne Kauf nutzbar.",
        "Zwei vollständige Einträge können kostenlos erstellt werden. Weitere Einträge erfordern ein automatisch verlängertes Monatsabo. Bestehende Einträge bleiben nach Abo-Ende nutzbar.",
        "Promise Guard prüft Eingaben nicht, stellt keinen Vertragsbruch fest und leistet keine Rechtsberatung. Berichte sind persönliche Übersichten aus Ihren Angaben.",
    ),
    "it": p(
        "Promesse sempre sotto mano",
        "Annota promesse, date e documenti, segui l'esito e prepara un riepilogo personale obiettivo. Senza account e senza pubblicità.",
        "Registra promesse, date ed esiti in locale, senza account né pubblicità.",
        "promessa,registro,promemoria,rapporto,rimborso,fornitore",
        "Una promessa di un fornitore non dovrebbe dipendere dalla memoria. Promise Guard offre uno spazio ordinato per registrarla e seguire ciò che accade.",
        ["Annota fornitore, parole esatte, canale, date, importo e riferimento", "Conserva la voce originale e aggiungi correzioni, aggiornamenti ed esiti con data", "Allega file di supporto e imposta promemoria privati", "Controlla subito registri aperti, in scadenza, risolti e archiviati", "Prepara un riepilogo personale di una pagina e rivedilo prima di condividerlo"],
        "Progettato per l'archiviazione locale: non servono account o server di contenuti GoodUse Studios. Niente pubblicità. Decidi tu se esportare, salvare o condividere.",
        "Crea due registri completi senza costi. Un acquisto in-app una tantum abilita la creazione di altri registri. Quelli esistenti restano utilizzabili senza l'acquisto.",
        "Crea due registri completi senza costi. Per crearne altri serve un abbonamento mensile con rinnovo automatico. Quelli esistenti restano utilizzabili alla fine dell'abbonamento.",
        "Promise Guard non verifica le voci, non stabilisce violazioni e non offre consulenza legale. I rapporti sono riepiloghi personali basati sui tuoi dati.",
    ),
    "nl": p(
        "Leg toezeggingen helder vast",
        "Leg toezeggingen, datums en stukken vast, volg de uitkomst en maak een feitelijk persoonlijk overzicht. Zonder account of advertenties.",
        "Leg toezeggingen, datums en uitkomsten lokaal vast, zonder account of reclame.",
        "toezegging,dossier,herinnering,rapport,terugbetaling",
        "Een toezegging van een aanbieder hoort niet van uw geheugen af te hangen. Promise Guard biedt een rustige, geordende plek voor de toezegging en het vervolg.",
        ["Noteer aanbieder, exacte woorden, kanaal, datums, bedrag en referentie", "Bewaar de oorspronkelijke invoer en voeg gedateerde correcties, updates en uitkomsten toe", "Voeg ondersteunende stukken toe en stel privéherinneringen in", "Bekijk openstaande, naderende, afgehandelde en gearchiveerde dossiers", "Maak een feitelijk persoonlijk overzicht van één pagina en controleer het voor delen"],
        "Lokaal ontworpen: geen GoodUse Studios-account of inhoudsserver vereist. Geen advertenties. U bepaalt of en waar u exporteert, een back-up maakt of deelt.",
        "Maak twee volledige dossiers zonder kosten. Met een eenmalige in-appaankoop kunt u meer dossiers maken. Bestaande dossiers blijven bruikbaar zonder de aankoop.",
        "Maak twee volledige dossiers zonder kosten. Voor meer dossiers is een automatisch verlengd maandabonnement nodig. Bestaande dossiers blijven bruikbaar nadat het abonnement eindigt.",
        "Promise Guard verifieert invoer niet, stelt geen tekortkoming vast en geeft geen juridisch advies. Rapporten zijn persoonlijke overzichten op basis van uw invoer.",
    ),
    "pl": p(
        "Zapisuj obietnice jasno",
        "Zapisuj obietnice, terminy i materiały, śledź rezultat i przygotuj rzeczowe podsumowanie. Bez konta i reklam.",
        "Zapisuj obietnice, terminy i wyniki lokalnie, bez konta i reklam.",
        "obietnica,zapis,przypomnienie,raport,zwrot,firma",
        "Obietnica firmy nie powinna zależeć wyłącznie od pamięci. Promise Guard zapewnia spokojne, uporządkowane miejsce na zapis i dalszy przebieg sprawy.",
        ["Zapisz firmę, dokładne słowa, kanał, terminy, kwotę i numer sprawy", "Zachowaj wpis pierwotny i dodawaj datowane korekty, aktualizacje oraz wyniki", "Dołącz materiały pomocnicze i ustaw prywatne przypomnienia", "Szybko sprawdzaj sprawy otwarte, pilne, rozwiązane i zarchiwizowane", "Przygotuj jednostronicowe rzeczowe podsumowanie i sprawdź je przed udostępnieniem"],
        "Dane są przechowywane lokalnie: konto ani serwer treści GoodUse Studios nie są wymagane. Bez reklam. Ty decydujesz o eksporcie, kopii i udostępnieniu.",
        "Utwórz bezpłatnie dwa pełne wpisy. Jednorazowy zakup w aplikacji odblokowuje tworzenie kolejnych. Istniejące wpisy pozostają dostępne bez zakupu.",
        "Utwórz bezpłatnie dwa pełne wpisy. Kolejne wymagają automatycznie odnawianej subskrypcji miesięcznej. Istniejące wpisy pozostają dostępne po jej zakończeniu.",
        "Promise Guard nie weryfikuje wpisów, nie stwierdza naruszenia i nie udziela porad prawnych. Raporty są osobistymi podsumowaniami z Twoich danych.",
    ),
    "tr": p(
        "Sözleri net biçimde kaydedin",
        "Verilen sözü, tarihleri ve belgeleri kaydedin; sonucu izleyip nesnel bir özet hazırlayın. Hesap ve reklam yok.",
        "Verilen sözleri, tarihleri ve sonuçları hesap ya da reklam olmadan kaydedin.",
        "söz,kayıt,hatırlatıcı,rapor,iade,sağlayıcı",
        "Bir hizmet sağlayıcının verdiği söz yalnızca hafızanıza bağlı kalmamalı. Promise Guard, sözü ve sonrasında yaşananları düzenli biçimde kaydetmenizi sağlar.",
        ["Sağlayıcıyı, tam ifadeyi, kanalı, tarihleri, tutarı ve referansı kaydedin", "İlk kaydı koruyup tarihli düzeltmeler, güncellemeler ve sonuçlar ekleyin", "Destekleyici dosyalar ekleyin ve özel hatırlatıcılar ayarlayın", "Açık, yaklaşan, çözülen ve arşivlenen kayıtları görün", "Tek sayfalık nesnel kişisel özeti paylaşmadan önce inceleyin"],
        "Yerel depolama odaklıdır: GoodUse Studios hesabı veya içerik sunucusu gerekmez. Reklam yoktur. Dışa aktarma, yedekleme ve paylaşma sizin seçiminizdir.",
        "İki tam kaydı ücretsiz oluşturun. Tek seferlik uygulama içi satın alma daha fazla kayıt oluşturmayı açar. Mevcut kayıtlar satın alma olmadan kullanılabilir.",
        "İki tam kaydı ücretsiz oluşturun. Daha fazlası için otomatik yenilenen aylık abonelik gerekir. Abonelik bittiğinde mevcut kayıtlar kullanılabilir.",
        "Promise Guard girdileri doğrulamaz, sözün ihlal edildiğine karar vermez ve hukuki danışmanlık sunmaz. Raporlar, girdilerinizden oluşan kişisel özetlerdir.",
    ),
    "ro": p(
        "Păstrează promisiunile clare",
        "Notează promisiunea, datele și documentele, urmărește rezultatul și pregătește un rezumat factual. Fără cont și reclame.",
        "Notează promisiuni, termene și rezultate local, fără cont sau reclame.",
        "promisiune,înregistrare,memento,raport,rambursare",
        "O promisiune făcută de un furnizor nu ar trebui să depindă de memorie. Promise Guard oferă un loc ordonat pentru promisiune și evoluția ei.",
        ["Notează furnizorul, formularea exactă, canalul, datele, suma și referința", "Păstrează intrarea inițială și adaugă corecții, actualizări și rezultate datate", "Atașează fișiere de sprijin și setează mementouri private", "Vezi rapid înregistrările deschise, scadente, rezolvate și arhivate", "Pregătește un rezumat personal factual de o pagină și verifică-l înainte de partajare"],
        "Conceput pentru stocare locală: nu este necesar un cont sau un server de conținut GoodUse Studios. Fără reclame. Tu alegi dacă exporți, salvezi sau partajezi.",
        "Creează gratuit două înregistrări complete. O achiziție unică în aplicație deblochează altele. Înregistrările existente rămân utilizabile fără achiziție.",
        "Creează gratuit două înregistrări complete. Pentru altele este necesar un abonament lunar cu reînnoire automată. Înregistrările existente rămân utilizabile după încheierea abonamentului.",
        "Promise Guard nu verifică intrările, nu stabilește încălcarea unei promisiuni și nu oferă consultanță juridică. Rapoartele sunt rezumate personale din datele tale.",
    ),
    "cs": p(
        "Mějte sliby přehledně",
        "Zapište slib, termíny a podklady, sledujte výsledek a připravte věcné shrnutí. Bez účtu a reklam.",
        "Zapisujte sliby, termíny a výsledky místně, bez účtu a reklam.",
        "slib,záznam,připomínka,zpráva,vrácení,služba",
        "Slib poskytovatele by neměl záviset jen na paměti. Promise Guard nabízí klidné a uspořádané místo pro slib i další vývoj.",
        ["Zapište poskytovatele, přesné znění, kanál, termíny, částku a referenci", "Uchovejte původní zápis a přidávejte datované opravy, změny a výsledky", "Přiložte podpůrné soubory a nastavte soukromé připomínky", "Sledujte otevřené, blížící se, vyřešené a archivované záznamy", "Připravte jednostránkové věcné osobní shrnutí a před sdílením je zkontrolujte"],
        "Navrženo pro místní ukládání: účet ani obsahový server GoodUse Studios nejsou nutné. Bez reklam. O exportu, záloze a sdílení rozhodujete vy.",
        "Dva úplné záznamy vytvoříte zdarma. Jednorázový nákup v aplikaci odemkne další. Existující záznamy zůstávají dostupné i bez nákupu.",
        "Dva úplné záznamy vytvoříte zdarma. Další vyžadují automaticky obnovované měsíční předplatné. Existující záznamy zůstávají dostupné i po jeho skončení.",
        "Promise Guard záznamy neověřuje, nerozhoduje o porušení slibu a neposkytuje právní rady. Zprávy jsou osobní shrnutí vytvořená z vašich údajů.",
    ),
    "uk": p(
        "Фіксуйте обіцянки чітко",
        "Записуйте обіцянки, дати й матеріали, відстежуйте результат і готуйте фактичний підсумок. Без облікового запису та реклами.",
        "Записуйте обіцянки, строки й результати локально, без акаунта та реклами.",
        "обіцянка,запис,нагадування,звіт,повернення",
        "Обіцянка постачальника не має залежати лише від пам’яті. Promise Guard дає впорядковане місце для запису обіцянки та подальших подій.",
        ["Запишіть постачальника, точні слова, канал, дати, суму й номер звернення", "Збережіть початковий запис і додавайте датовані виправлення, зміни та результати", "Долучайте допоміжні файли й установлюйте приватні нагадування", "Переглядайте відкриті, термінові, вирішені й архівні записи", "Створіть односторінковий фактичний особистий підсумок і перевірте його перед поширенням"],
        "Локальне зберігання за задумом: обліковий запис чи сервер вмісту GoodUse Studios не потрібні. Без реклами. Ви вирішуєте, чи експортувати, копіювати або поширювати.",
        "Створіть два повні записи безкоштовно. Одноразова покупка в застосунку відкриває створення наступних. Наявні записи залишаються доступними без покупки.",
        "Створіть два повні записи безкоштовно. Для наступних потрібна щомісячна підписка з автопоновленням. Наявні записи залишаються доступними після її завершення.",
        "Promise Guard не перевіряє записи, не встановлює порушення обіцянки й не надає юридичних порад. Звіти — особисті підсумки на основі ваших даних.",
    ),
    "ru": p(
        "Фиксируйте обещания чётко",
        "Записывайте обещания, даты и материалы, отслеживайте результат и готовьте фактическую сводку. Без аккаунта и рекламы.",
        "Записывайте обещания, сроки и результаты локально, без аккаунта и рекламы.",
        "обещание,запись,напоминание,отчёт,возврат",
        "Обещание поставщика не должно зависеть только от памяти. Promise Guard даёт спокойное и упорядоченное место для записи обещания и дальнейших событий.",
        ["Запишите поставщика, точные слова, канал, даты, сумму и номер обращения", "Сохраните исходную запись и добавляйте датированные исправления, изменения и результаты", "Прикрепляйте сопроводительные материалы и ставьте личные напоминания", "Просматривайте открытые, срочные, решённые и архивные записи", "Подготовьте одностраничную фактическую личную сводку и проверьте её перед отправкой"],
        "Локальное хранение по умолчанию: аккаунт или сервер содержимого GoodUse Studios не требуется. Без рекламы. Вы решаете, экспортировать, копировать или передавать данные.",
        "Создайте две полные записи бесплатно. Однократная покупка в приложении открывает создание новых. Существующие записи доступны без покупки.",
        "Создайте две полные записи бесплатно. Для новых нужна ежемесячная подписка с автопродлением. Существующие записи доступны после её окончания.",
        "Promise Guard не проверяет записи, не устанавливает нарушение обещания и не даёт юридических советов. Отчёты — личные сводки на основе ваших данных.",
    ),
    "ar": p(
        "سجّل الوعود بوضوح",
        "سجّل الوعد والتواريخ والمواد الداعمة، وتابع النتيجة وأعد ملخصاً شخصياً موضوعياً، بلا حساب أو إعلانات.",
        "سجّل وعود الجهات ومواعيدها ونتائجها محلياً، بلا حساب أو إعلانات.",
        "وعد,سجل,تذكير,تقرير,استرداد",
        "لا ينبغي أن يعتمد وعد مقدّم الخدمة على الذاكرة وحدها. يمنحك Promise Guard مكاناً منظماً لتسجيل الوعد وما يحدث بعده.",
        ["سجّل الجهة والعبارة الدقيقة والقناة والتواريخ والمبلغ والمرجع", "احتفظ بالإدخال الأصلي وأضف تصحيحات وتحديثات ونتائج مؤرخة", "أرفق ملفات داعمة واضبط تذكيرات خاصة", "راجع السجلات المفتوحة والقريبة والمحلولة والمؤرشفة بسرعة", "أعد ملخصاً شخصياً موضوعياً من صفحة واحدة وراجعه قبل المشاركة"],
        "مصمم للتخزين المحلي: لا يلزم حساب أو خادم محتوى لدى GoodUse Studios. بلا إعلانات. أنت تختار التصدير أو النسخ الاحتياطي أو المشاركة.",
        "أنشئ سجلين كاملين دون تكلفة. تتيح عملية شراء واحدة داخل التطبيق إنشاء سجلات إضافية. تبقى السجلات الحالية قابلة للاستخدام دون الشراء.",
        "أنشئ سجلين كاملين دون تكلفة. يتطلب إنشاء المزيد اشتراكاً شهرياً متجدداً تلقائياً. تبقى السجلات الحالية قابلة للاستخدام بعد انتهاء الاشتراك.",
        "لا يتحقق Promise Guard من الإدخالات ولا يقرر وقوع إخلال ولا يقدم مشورة قانونية. التقارير ملخصات شخصية مبنية على بياناتك.",
    ),
    "zh-Hans": p(
        "清楚记录每个承诺",
        "记录服务商的承诺、日期和支持材料，跟进结果并制作客观的个人摘要。无需账户，无广告。",
        "本地记录服务商承诺、日期和结果，无需账户，无广告。",
        "承诺,记录,提醒,报告,退款,服务商",
        "服务商作出的承诺不应只靠记忆。Promise Guard 为承诺和后续进展提供清晰、有序的记录空间。",
        ["记录服务商、准确表述、沟通渠道、日期、金额和参考编号", "保留原始记录，并添加带日期的更正、更新和结果", "添加支持材料并设置私密提醒", "快速查看待处理、临近、已解决和已归档记录", "生成一页客观个人摘要，并在分享前核对"],
        "本地优先设计：无需 GoodUse Studios 账户或内容服务器。无广告。是否导出、备份或分享由你决定。",
        "可免费创建两条完整记录。一次性应用内购买可解锁更多记录的创建权限。未购买时，已有记录仍可使用。",
        "可免费创建两条完整记录。继续创建需按月自动续订。订阅结束后，已有记录仍可使用。",
        "Promise Guard 不核实输入内容、不判定是否违约，也不提供法律建议。报告仅是根据你的输入生成的个人摘要。",
    ),
    "zh-Hant": p(
        "清楚記錄每個承諾",
        "記錄服務商的承諾、日期和支援資料，追蹤結果並製作客觀的個人摘要。毋須帳戶，沒有廣告。",
        "在裝置上記錄服務商承諾、日期和結果，毋須帳戶，沒有廣告。",
        "承諾,記錄,提醒,報告,退款,服務商",
        "服務商作出的承諾不應只靠記憶。Promise Guard 為承諾及後續進展提供清楚、有序的記錄空間。",
        ["記錄服務商、準確字句、溝通渠道、日期、金額和參考編號", "保留原始記錄，並加入附有日期的更正、更新和結果", "加入支援資料並設定私人提醒", "快速查看待處理、即將到期、已解決和已封存記錄", "製作一頁客觀個人摘要，並在分享前核對"],
        "本機優先設計：毋須 GoodUse Studios 帳戶或內容伺服器。沒有廣告。是否匯出、備份或分享由你決定。",
        "可免費建立兩筆完整記錄。一次性 App 內購買可解鎖建立更多記錄。未購買時，現有記錄仍可使用。",
        "可免費建立兩筆完整記錄。繼續建立需每月自動續訂。訂閱結束後，現有記錄仍可使用。",
        "Promise Guard 不核實輸入內容、不判定是否違約，也不提供法律意見。報告只是根據你的輸入製作的個人摘要。",
    ),
    "ja": p(
        "約束を明確に記録",
        "事業者の約束、日付、参考資料を記録し、結果を追跡して事実に基づく個人用要約を作成。アカウント不要、広告なし。",
        "事業者の約束・期日・結果を端末内に記録。アカウント不要、広告なし。",
        "約束,記録,リマインダー,レポート,返金",
        "事業者から受けた約束を、記憶だけに頼らず整理できます。Promise Guard は約束とその後の経過を落ち着いて記録するための場所です。",
        ["事業者、正確な文言、連絡手段、日付、金額、参照番号を記録", "元の記録を残したまま、日付付きの訂正・更新・結果を追加", "参考資料を添付し、非公開のリマインダーを設定", "対応中、期限間近、解決済み、アーカイブ済みを一覧で確認", "1ページの事実ベースの個人用要約を作り、共有前に確認"],
        "ローカル保存を基本とし、GoodUse Studios のアカウントや記録内容用サーバーは不要です。広告はありません。書き出し、バックアップ、共有は利用者が選択します。",
        "完全な記録を2件まで無料で作成できます。1回限りのアプリ内購入で追加作成を解除できます。購入しなくても既存の記録は利用できます。",
        "完全な記録を2件まで無料で作成できます。追加作成には自動更新の月額サブスクリプションが必要です。終了後も既存の記録は利用できます。",
        "Promise Guard は入力内容を検証せず、約束違反を判断せず、法律相談を提供しません。レポートは入力内容に基づく個人用要約です。",
    ),
    "ko": p(
        "약속을 명확하게 기록",
        "업체의 약속과 날짜, 참고 자료를 기록하고 결과를 추적해 사실 중심의 개인 요약을 만드세요. 계정과 광고가 없습니다.",
        "업체의 약속·기한·결과를 기기에 기록하세요. 계정과 광고가 없습니다.",
        "약속,기록,알림,보고서,환불,업체",
        "업체가 한 약속을 기억에만 맡기지 마세요. Promise Guard는 약속과 이후 진행 상황을 차분하고 체계적으로 기록하는 공간입니다.",
        ["업체, 정확한 표현, 연락 경로, 날짜, 금액, 참조 번호 기록", "원본을 유지하고 날짜가 있는 정정, 변경, 결과 추가", "참고 자료를 첨부하고 비공개 알림 설정", "진행 중, 임박, 해결, 보관 기록을 한눈에 확인", "한 페이지의 사실 중심 개인 요약을 만들고 공유 전 검토"],
        "로컬 우선 설계로 GoodUse Studios 계정이나 기록 내용 서버가 필요하지 않습니다. 광고가 없습니다. 내보내기, 백업, 공유 여부는 사용자가 선택합니다.",
        "완전한 기록 2개를 무료로 만들 수 있습니다. 일회성 앱 내 구매로 추가 기록 생성을 잠금 해제합니다. 구매하지 않아도 기존 기록은 계속 사용할 수 있습니다.",
        "완전한 기록 2개를 무료로 만들 수 있습니다. 추가 생성에는 자동 갱신 월간 구독이 필요합니다. 구독 종료 후에도 기존 기록은 계속 사용할 수 있습니다.",
        "Promise Guard는 입력을 검증하거나 약속 위반을 판단하거나 법률 자문을 제공하지 않습니다. 보고서는 사용자의 입력으로 만든 개인 요약입니다.",
    ),
    "hi": p(
        "वादे स्पष्ट रूप से दर्ज करें",
        "कंपनी का वादा, तारीखें और सहायक सामग्री दर्ज करें, परिणाम देखें और तथ्यात्मक निजी सारांश बनाएँ। बिना खाते और विज्ञापन के।",
        "वादे, तारीखें और परिणाम डिवाइस पर दर्ज करें—बिना खाते या विज्ञापन के।",
        "वादा,रिकॉर्ड,रिमाइंडर,रिपोर्ट,रिफंड",
        "सेवा प्रदाता का वादा केवल याददाश्त पर निर्भर नहीं रहना चाहिए। Promise Guard वादे और आगे की घटनाओं को व्यवस्थित रूप से दर्ज करने की जगह देता है।",
        ["प्रदाता, सटीक शब्द, माध्यम, तारीख, राशि और संदर्भ दर्ज करें", "मूल प्रविष्टि सुरक्षित रखें और तारीख वाली सुधार, जानकारी व परिणाम जोड़ें", "सहायक फ़ाइलें जोड़ें और निजी रिमाइंडर तय करें", "खुले, निकट, हल किए और संग्रहित रिकॉर्ड एक नज़र में देखें", "एक पृष्ठ का तथ्यात्मक निजी सारांश बनाएँ और साझा करने से पहले जाँचें"],
        "स्थानीय संग्रह के लिए बनाया गया: GoodUse Studios खाता या रिकॉर्ड-सामग्री सर्वर आवश्यक नहीं। कोई विज्ञापन नहीं। निर्यात, बैकअप या साझा करना आपकी पसंद है।",
        "दो पूरे रिकॉर्ड बिना शुल्क बनाएँ। एक बार की इन-ऐप खरीद से और रिकॉर्ड बनाना खुलता है। खरीद के बिना भी मौजूदा रिकॉर्ड उपयोग योग्य रहते हैं।",
        "दो पूरे रिकॉर्ड बिना शुल्क बनाएँ। और रिकॉर्ड बनाने के लिए अपने-आप नवीनीकृत मासिक सदस्यता चाहिए। सदस्यता समाप्त होने पर भी मौजूदा रिकॉर्ड उपयोग योग्य रहते हैं।",
        "Promise Guard प्रविष्टियों की पुष्टि नहीं करता, उल्लंघन का निर्णय नहीं देता और कानूनी सलाह नहीं देता। रिपोर्ट आपके डेटा से बने निजी सारांश हैं।",
    ),
    "ur": p(
        "وعدے واضح طور پر درج کریں",
        "ادارے کا وعدہ، تاریخیں اور معاون مواد درج کریں، نتیجہ دیکھیں اور حقائق پر مبنی ذاتی خلاصہ بنائیں۔ اکاؤنٹ اور اشتہارات کے بغیر۔",
        "وعدے، تاریخیں اور نتائج فون پر درج کریں، بغیر اکاؤنٹ یا اشتہارات کے۔",
        "وعدہ,ریکارڈ,یاددہانی,رپورٹ,رقم واپسی",
        "خدمت فراہم کرنے والے کا وعدہ صرف یادداشت پر منحصر نہیں ہونا چاہیے۔ Promise Guard وعدے اور بعد کی پیش رفت کو منظم طور پر درج کرنے کی جگہ دیتا ہے۔",
        ["ادارہ، اصل الفاظ، رابطے کا ذریعہ، تاریخیں، رقم اور حوالہ درج کریں", "اصل اندراج محفوظ رکھیں اور تاریخ والی تصحیح، تبدیلیاں اور نتائج شامل کریں", "معاون فائلیں شامل کریں اور نجی یاددہانیاں مقرر کریں", "کھلے، قریب، حل شدہ اور محفوظ شدہ ریکارڈ ایک نظر میں دیکھیں", "ایک صفحے کا حقائق پر مبنی ذاتی خلاصہ بنائیں اور شیئر کرنے سے پہلے جانچیں"],
        "مقامی ذخیرے کے لیے بنایا گیا: GoodUse Studios اکاؤنٹ یا مواد کا سرور درکار نہیں۔ اشتہارات نہیں۔ برآمد، بیک اپ یا شیئر کرنا آپ کی مرضی ہے۔",
        "دو مکمل ریکارڈ بلا معاوضہ بنائیں۔ ایک بار کی ایپ خرید سے مزید ریکارڈ بنانا کھلتا ہے۔ موجودہ ریکارڈ خرید کے بغیر بھی دستیاب رہتے ہیں۔",
        "دو مکمل ریکارڈ بلا معاوضہ بنائیں۔ مزید ریکارڈ کے لیے خودکار ماہانہ رکنیت درکار ہے۔ رکنیت ختم ہونے پر موجودہ ریکارڈ دستیاب رہتے ہیں۔",
        "Promise Guard اندراجات کی تصدیق، وعدہ خلافی کا فیصلہ یا قانونی مشورہ نہیں دیتا۔ رپورٹس آپ کے اندراجات سے بنے ذاتی خلاصے ہیں۔",
    ),
    "bn": p(
        "প্রতিশ্রুতি স্পষ্টভাবে লিখুন",
        "প্রতিষ্ঠানের প্রতিশ্রুতি, তারিখ ও সহায়ক উপকরণ লিখুন, ফলাফল দেখুন এবং তথ্যভিত্তিক ব্যক্তিগত সারাংশ তৈরি করুন। অ্যাকাউন্ট ও বিজ্ঞাপন ছাড়া।",
        "প্রতিশ্রুতি, তারিখ ও ফলাফল ডিভাইসে লিখুন—অ্যাকাউন্ট বা বিজ্ঞাপন ছাড়া।",
        "প্রতিশ্রুতি,রেকর্ড,স্মরণিকা,প্রতিবেদন,ফেরত",
        "সেবা প্রদানকারীর প্রতিশ্রুতি শুধু স্মৃতির ওপর নির্ভর করা উচিত নয়। Promise Guard প্রতিশ্রুতি ও পরবর্তী ঘটনাগুলো গুছিয়ে রাখার জায়গা দেয়।",
        ["প্রদানকারী, সঠিক ভাষা, মাধ্যম, তারিখ, অর্থ ও রেফারেন্স লিখুন", "মূল এন্ট্রি রেখে তারিখসহ সংশোধন, হালনাগাদ ও ফলাফল যোগ করুন", "সহায়ক ফাইল যোগ করুন এবং ব্যক্তিগত স্মরণিকা ঠিক করুন", "খোলা, আসন্ন, সমাধান ও আর্কাইভ করা রেকর্ড এক নজরে দেখুন", "এক পাতার তথ্যভিত্তিক ব্যক্তিগত সারাংশ বানিয়ে ভাগ করার আগে যাচাই করুন"],
        "স্থানীয় সংরক্ষণভিত্তিক: GoodUse Studios অ্যাকাউন্ট বা রেকর্ডের সার্ভার লাগে না। বিজ্ঞাপন নেই। রপ্তানি, ব্যাকআপ ও ভাগ করা আপনার সিদ্ধান্ত।",
        "দুটি পূর্ণ রেকর্ড বিনা খরচে তৈরি করুন। এককালীন ইন-অ্যাপ ক্রয়ে আরও রেকর্ড তৈরি করা যাবে। ক্রয় ছাড়াও আগের রেকর্ড ব্যবহারযোগ্য থাকবে।",
        "দুটি পূর্ণ রেকর্ড বিনা খরচে তৈরি করুন। আরও রেকর্ডের জন্য স্বয়ংক্রিয় মাসিক সাবস্ক্রিপশন লাগে। সাবস্ক্রিপশন শেষ হলেও আগের রেকর্ড ব্যবহারযোগ্য থাকবে।",
        "Promise Guard এন্ট্রি যাচাই করে না, প্রতিশ্রুতি ভঙ্গের সিদ্ধান্ত দেয় না এবং আইনি পরামর্শ দেয় না। প্রতিবেদন আপনার তথ্য থেকে তৈরি ব্যক্তিগত সারাংশ।",
    ),
    "vi": p(
        "Ghi lời hứa thật rõ ràng",
        "Ghi lời hứa, ngày tháng và tài liệu hỗ trợ; theo dõi kết quả và tạo bản tóm tắt khách quan. Không tài khoản, không quảng cáo.",
        "Ghi lời hứa, thời hạn và kết quả trên máy, không tài khoản hay quảng cáo.",
        "lời hứa,hồ sơ,nhắc việc,báo cáo,hoàn tiền",
        "Lời hứa của nhà cung cấp không nên chỉ dựa vào trí nhớ. Promise Guard tạo một nơi rõ ràng để ghi lại lời hứa và diễn biến sau đó.",
        ["Ghi nhà cung cấp, lời nói chính xác, kênh liên hệ, ngày, số tiền và mã tham chiếu", "Giữ nguyên bản ghi đầu tiên và thêm sửa đổi, cập nhật, kết quả có ngày", "Đính kèm tài liệu hỗ trợ và đặt nhắc việc riêng tư", "Xem nhanh hồ sơ đang mở, sắp đến hạn, đã giải quyết và lưu trữ", "Tạo bản tóm tắt cá nhân một trang và kiểm tra trước khi chia sẻ"],
        "Ưu tiên lưu trên thiết bị: không cần tài khoản hay máy chủ nội dung của GoodUse Studios. Không quảng cáo. Bạn quyết định việc xuất, sao lưu hoặc chia sẻ.",
        "Tạo miễn phí hai hồ sơ đầy đủ. Mua một lần trong ứng dụng để mở khóa việc tạo thêm. Hồ sơ hiện có vẫn dùng được khi chưa mua.",
        "Tạo miễn phí hai hồ sơ đầy đủ. Muốn tạo thêm cần gói thuê bao tháng tự động gia hạn. Hồ sơ hiện có vẫn dùng được khi thuê bao kết thúc.",
        "Promise Guard không xác minh nội dung, không kết luận vi phạm lời hứa và không tư vấn pháp lý. Báo cáo là tóm tắt cá nhân từ dữ liệu của bạn.",
    ),
    "id": p(
        "Catat janji dengan jelas",
        "Catat janji, tanggal, dan dokumen pendukung; pantau hasil dan buat ringkasan faktual. Tanpa akun dan iklan.",
        "Catat janji, tenggat, dan hasil di perangkat, tanpa akun atau iklan.",
        "janji,catatan,pengingat,laporan,pengembalian",
        "Janji penyedia layanan tidak seharusnya hanya mengandalkan ingatan. Promise Guard menyediakan tempat rapi untuk mencatat janji dan perkembangannya.",
        ["Catat penyedia, kata-kata tepat, kanal, tanggal, jumlah, dan referensi", "Simpan entri awal lalu tambahkan koreksi, pembaruan, dan hasil bertanggal", "Lampirkan catatan pendukung dan atur pengingat pribadi", "Lihat catatan terbuka, mendekati jatuh tempo, selesai, dan diarsipkan", "Buat ringkasan pribadi faktual satu halaman dan tinjau sebelum dibagikan"],
        "Mengutamakan penyimpanan lokal: akun atau server konten GoodUse Studios tidak diperlukan. Tanpa iklan. Anda memilih ekspor, cadangan, dan berbagi.",
        "Buat dua catatan lengkap tanpa biaya. Pembelian dalam aplikasi satu kali membuka pembuatan catatan tambahan. Catatan lama tetap dapat digunakan tanpa membeli.",
        "Buat dua catatan lengkap tanpa biaya. Catatan tambahan memerlukan langganan bulanan yang diperpanjang otomatis. Catatan lama tetap dapat digunakan setelah langganan berakhir.",
        "Promise Guard tidak memverifikasi entri, menentukan pelanggaran janji, atau memberi nasihat hukum. Laporan adalah ringkasan pribadi dari data Anda.",
    ),
    "th": p(
        "บันทึกคำมั่นให้ชัดเจน",
        "บันทึกคำมั่น วันที่ และเอกสารประกอบ ติดตามผลและสร้างสรุปส่วนตัวตามข้อเท็จจริง โดยไม่ต้องมีบัญชีและไม่มีโฆษณา",
        "บันทึกคำมั่น กำหนดเวลา และผลไว้ในเครื่อง ไม่ต้องมีบัญชี ไม่มีโฆษณา",
        "คำมั่น,บันทึก,เตือน,รายงาน,คืนเงิน",
        "คำมั่นจากผู้ให้บริการไม่ควรต้องพึ่งความจำเพียงอย่างเดียว Promise Guard ช่วยจัดเก็บคำมั่นและความคืบหน้าอย่างเป็นระบบ",
        ["บันทึกผู้ให้บริการ ถ้อยคำ ช่องทาง วันที่ จำนวนเงิน และเลขอ้างอิง", "เก็บรายการเดิมไว้และเพิ่มการแก้ไข ข้อมูลใหม่ และผลพร้อมวันที่", "แนบไฟล์ประกอบและตั้งการเตือนส่วนตัว", "ดูรายการที่เปิด ใกล้ครบกำหนด แก้ไขแล้ว และเก็บถาวร", "สร้างสรุปส่วนตัวหนึ่งหน้าตามข้อเท็จจริงและตรวจสอบก่อนแชร์"],
        "ออกแบบให้เก็บในเครื่องเป็นหลัก ไม่ต้องมีบัญชีหรือเซิร์ฟเวอร์เนื้อหาของ GoodUse Studios ไม่มีโฆษณา คุณเลือกเองว่าจะส่งออก สำรอง หรือแชร์",
        "สร้างบันทึกฉบับสมบูรณ์ได้ฟรีสองรายการ การซื้อในแอปครั้งเดียวปลดล็อกการสร้างเพิ่มเติม รายการเดิมยังใช้ได้หากไม่ซื้อ",
        "สร้างบันทึกฉบับสมบูรณ์ได้ฟรีสองรายการ การสร้างเพิ่มเติมต้องสมัครสมาชิกรายเดือนแบบต่ออายุอัตโนมัติ รายการเดิมยังใช้ได้เมื่อสมาชิกสิ้นสุด",
        "Promise Guard ไม่ตรวจสอบข้อมูล ไม่ตัดสินว่าผิดคำมั่น และไม่ให้คำปรึกษากฎหมาย รายงานคือสรุปส่วนตัวจากข้อมูลของคุณ",
    ),
    "fil": p(
        "Malinaw na tala ng pangako",
        "Itala ang pangako, petsa at supporting files; subaybayan ang resulta at gumawa ng factual na buod. Walang account o ads.",
        "Itala sa device ang pangako, deadline at resulta—walang account o ads.",
        "pangako,tala,paalala,report,refund,provider",
        "Hindi dapat memorya lang ang sandigan sa pangako ng provider. Binibigyan ka ng Promise Guard ng maayos na lugar para itala ang pangako at mga sumunod na pangyayari.",
        ["Itala ang provider, eksaktong sinabi, channel, petsa, halaga at reference", "Panatilihin ang unang entry at magdagdag ng may petsang correction, update at resulta", "Mag-attach ng supporting files at magtakda ng pribadong paalala", "Tingnan ang open, malapit na, resolved at archived na records", "Gumawa ng isang-pahinang factual na personal summary at suriin bago i-share"],
        "Local-first: hindi kailangan ng GoodUse Studios account o content server. Walang ads. Ikaw ang pipili kung mag-export, mag-backup o mag-share.",
        "Gumawa ng dalawang kumpletong record nang walang bayad. Isang beses na in-app purchase ang magbubukas ng dagdag na records. Magagamit pa rin ang dating records kung hindi bumili.",
        "Gumawa ng dalawang kumpletong record nang walang bayad. Kailangan ng auto-renewing monthly subscription para sa dagdag. Magagamit pa rin ang dating records kapag natapos ang subscription.",
        "Hindi bine-verify ng Promise Guard ang entries, hindi ito nagpapasya kung may paglabag, at hindi nagbibigay ng legal advice. Personal summaries mula sa data mo ang reports.",
    ),
    "ms": p(
        "Catat janji dengan jelas",
        "Catat janji, tarikh dan bahan sokongan; ikuti hasil dan sediakan ringkasan fakta. Tanpa akaun dan iklan.",
        "Catat janji, tarikh akhir dan hasil pada peranti, tanpa akaun atau iklan.",
        "janji,rekod,peringatan,laporan,bayaran balik",
        "Janji penyedia tidak sepatutnya bergantung pada ingatan sahaja. Promise Guard menyediakan ruang tersusun untuk merekod janji dan perkembangan seterusnya.",
        ["Rekod penyedia, kata tepat, saluran, tarikh, amaun dan rujukan", "Kekalkan entri asal dan tambah pembetulan, kemas kini dan hasil bertarikh", "Lampirkan fail sokongan dan tetapkan peringatan peribadi", "Lihat rekod terbuka, hampir tiba, selesai dan diarkibkan", "Sediakan ringkasan peribadi satu halaman berdasarkan fakta dan semak sebelum berkongsi"],
        "Mengutamakan storan setempat: akaun atau pelayan kandungan GoodUse Studios tidak diperlukan. Tiada iklan. Anda memilih untuk mengeksport, menyandar atau berkongsi.",
        "Cipta dua rekod lengkap tanpa caj. Pembelian dalam aplikasi sekali sahaja membuka penciptaan tambahan. Rekod sedia ada kekal boleh digunakan tanpa pembelian.",
        "Cipta dua rekod lengkap tanpa caj. Rekod tambahan memerlukan langganan bulanan yang diperbaharui automatik. Rekod sedia ada kekal boleh digunakan selepas langganan tamat.",
        "Promise Guard tidak mengesahkan entri, menentukan pelanggaran janji atau memberi nasihat undang-undang. Laporan ialah ringkasan peribadi daripada data anda.",
    ),
    "fi": p(
        "Pidä lupaukset selkeinä",
        "Kirjaa lupaus, päivät ja tukitiedot, seuraa tulosta ja laadi asiallinen henkilökohtainen yhteenveto. Ei tiliä tai mainoksia.",
        "Kirjaa lupaukset, määräajat ja tulokset laitteelle ilman tiliä tai mainoksia.",
        "lupaus,muistiinpano,muistutus,raportti,palautus",
        "Palveluntarjoajan lupauksen ei pitäisi olla pelkän muistin varassa. Promise Guard tarjoaa selkeän paikan lupaukselle ja myöhemmille tapahtumille.",
        ["Kirjaa tarjoaja, tarkka sanamuoto, kanava, päivät, summa ja viite", "Säilytä alkuperäinen merkintä ja lisää päivätyt korjaukset, päivitykset ja tulokset", "Liitä tukitiedostoja ja aseta yksityisiä muistutuksia", "Näe avoimet, lähestyvät, ratkaistut ja arkistoidut merkinnät", "Laadi yhden sivun asiallinen henkilökohtainen yhteenveto ja tarkista se ennen jakamista"],
        "Paikallinen tallennus ensin: GoodUse Studios -tiliä tai sisältöpalvelinta ei tarvita. Ei mainoksia. Päätät itse viennistä, varmuuskopioinnista ja jakamisesta.",
        "Luo kaksi täydellistä merkintää maksutta. Kertaluonteinen sovelluksen sisäinen osto avaa lisämerkinnät. Nykyiset merkinnät toimivat ilman ostoa.",
        "Luo kaksi täydellistä merkintää maksutta. Lisämerkinnät vaativat automaattisesti uusiutuvan kuukausitilauksen. Nykyiset merkinnät toimivat tilauksen päätyttyä.",
        "Promise Guard ei vahvista merkintöjä, ratkaise lupauksen rikkomista eikä anna oikeudellista neuvontaa. Raportit ovat henkilökohtaisia yhteenvetoja tiedoistasi.",
    ),
    "sv": p(
        "Håll löften tydligt samlade",
        "Anteckna löften, datum och underlag, följ resultatet och skapa en saklig personlig sammanfattning. Utan konto eller reklam.",
        "Spara löften, tidsfrister och resultat lokalt, utan konto eller reklam.",
        "löfte,anteckning,påminnelse,rapport,återbetalning",
        "Ett löfte från en leverantör ska inte vara beroende av minnet. Promise Guard ger en lugn och ordnad plats för löftet och det som händer sedan.",
        ["Anteckna leverantör, exakt formulering, kanal, datum, belopp och referens", "Behåll originalet och lägg till daterade rättelser, uppdateringar och resultat", "Bifoga stödmaterial och ställ in privata påminnelser", "Se öppna, kommande, lösta och arkiverade poster", "Skapa en saklig personlig sammanfattning på en sida och granska före delning"],
        "Lokalt som grund: inget GoodUse Studios-konto eller innehållsserver krävs. Ingen reklam. Du bestämmer om export, säkerhetskopiering och delning.",
        "Skapa två fullständiga poster utan kostnad. Ett engångsköp i appen låser upp fler. Befintliga poster kan användas utan köpet.",
        "Skapa två fullständiga poster utan kostnad. Fler kräver en automatiskt förnyad månadsprenumeration. Befintliga poster kan användas när prenumerationen upphör.",
        "Promise Guard verifierar inte uppgifter, avgör inte avtalsbrott och ger inte juridisk rådgivning. Rapporter är personliga sammanfattningar av dina uppgifter.",
    ),
    "da": p(
        "Hold løfter klart samlet",
        "Notér løfter, datoer og bilag, følg resultatet og lav et sagligt personligt resumé. Uden konto eller reklamer.",
        "Gem løfter, frister og resultater lokalt, uden konto eller reklamer.",
        "løfte,notat,påmindelse,rapport,tilbagebetaling",
        "Et løfte fra en leverandør bør ikke afhænge af hukommelsen. Promise Guard giver et roligt og ordnet sted til løftet og det videre forløb.",
        ["Notér leverandør, præcis ordlyd, kanal, datoer, beløb og reference", "Bevar den oprindelige post og tilføj daterede rettelser, opdateringer og resultater", "Vedhæft støttende filer og indstil private påmindelser", "Se åbne, kommende, løste og arkiverede poster", "Lav et sagligt personligt resumé på én side og gennemgå det før deling"],
        "Lokalt som udgangspunkt: ingen GoodUse Studios-konto eller indholdsserver kræves. Ingen reklamer. Du vælger eksport, sikkerhedskopi og deling.",
        "Opret to komplette poster uden betaling. Et engangskøb i appen åbner for flere. Eksisterende poster kan bruges uden købet.",
        "Opret to komplette poster uden betaling. Flere kræver et automatisk fornyet månedsabonnement. Eksisterende poster kan bruges efter abonnementets ophør.",
        "Promise Guard kontrollerer ikke indtastninger, afgør ikke løftebrud og yder ikke juridisk rådgivning. Rapporter er personlige resuméer af dine data.",
    ),
    "nb": p(
        "Hold løfter tydelig samlet",
        "Noter løfter, datoer og vedlegg, følg resultatet og lag et saklig personlig sammendrag. Uten konto eller reklame.",
        "Lagre løfter, frister og resultater lokalt, uten konto eller reklame.",
        "løfte,notat,påminnelse,rapport,tilbakebetaling",
        "Et løfte fra en leverandør bør ikke være avhengig av hukommelsen. Promise Guard gir et rolig og ryddig sted for løftet og det som skjer videre.",
        ["Noter leverandør, nøyaktig ordlyd, kanal, datoer, beløp og referanse", "Behold originalen og legg til daterte rettelser, oppdateringer og resultater", "Legg ved støttemateriale og angi private påminnelser", "Se åpne, kommende, løste og arkiverte poster", "Lag et saklig personlig sammendrag på én side og kontroller før deling"],
        "Lokalt som utgangspunkt: ingen GoodUse Studios-konto eller innholdsserver kreves. Ingen reklame. Du velger eksport, sikkerhetskopi og deling.",
        "Opprett to komplette poster uten kostnad. Et engangskjøp i appen åpner for flere. Eksisterende poster kan brukes uten kjøpet.",
        "Opprett to komplette poster uten kostnad. Flere krever et automatisk fornyet månedsabonnement. Eksisterende poster kan brukes etter at abonnementet avsluttes.",
        "Promise Guard kontrollerer ikke oppføringer, avgjør ikke løftebrudd og gir ikke juridisk rådgivning. Rapporter er personlige sammendrag av dine data.",
    ),
    "el": p(
        "Σαφής καταγραφή υποσχέσεων",
        "Καταγράψτε υποσχέσεις, ημερομηνίες και υλικό, παρακολουθήστε το αποτέλεσμα και ετοιμάστε αντικειμενική σύνοψη. Χωρίς λογαριασμό ή διαφημίσεις.",
        "Καταγράψτε υποσχέσεις και αποτελέσματα χωρίς λογαριασμό ή διαφημίσεις.",
        "υπόσχεση,αρχείο,υπενθύμιση,αναφορά,επιστροφή",
        "Μια υπόσχεση παρόχου δεν πρέπει να βασίζεται μόνο στη μνήμη. Το Promise Guard προσφέρει οργανωμένο χώρο για την υπόσχεση και όσα ακολουθούν.",
        ["Καταγράψτε πάροχο, ακριβή λόγια, κανάλι, ημερομηνίες, ποσό και αναφορά", "Διατηρήστε την αρχική εγγραφή και προσθέστε χρονολογημένες διορθώσεις, ενημερώσεις και αποτελέσματα", "Επισυνάψτε υποστηρικτικό υλικό και ορίστε ιδιωτικές υπενθυμίσεις", "Δείτε ανοιχτές, επερχόμενες, λυμένες και αρχειοθετημένες εγγραφές", "Ετοιμάστε μονοσέλιδη αντικειμενική προσωπική σύνοψη και ελέγξτε πριν την κοινοποίηση"],
        "Με τοπική αποθήκευση: δεν απαιτείται λογαριασμός ή διακομιστής περιεχομένου GoodUse Studios. Χωρίς διαφημίσεις. Εσείς επιλέγετε εξαγωγή, αντίγραφο ή κοινοποίηση.",
        "Δημιουργήστε δύο πλήρεις εγγραφές χωρίς χρέωση. Μία εφάπαξ αγορά εντός εφαρμογής ξεκλειδώνει περισσότερες. Οι υπάρχουσες παραμένουν διαθέσιμες χωρίς αγορά.",
        "Δημιουργήστε δύο πλήρεις εγγραφές χωρίς χρέωση. Για περισσότερες απαιτείται μηνιαία συνδρομή με αυτόματη ανανέωση. Οι υπάρχουσες παραμένουν διαθέσιμες μετά τη λήξη.",
        "Το Promise Guard δεν επαληθεύει εγγραφές, δεν κρίνει παραβίαση υπόσχεσης και δεν παρέχει νομικές συμβουλές. Οι αναφορές είναι προσωπικές συνόψεις των δεδομένων σας.",
    ),
    "he": p(
        "תיעוד ברור של הבטחות",
        "תעדו את ההבטחה, התאריכים והחומרים התומכים, עקבו אחר התוצאה והכינו סיכום אישי עובדתי. בלי חשבון ובלי פרסומות.",
        "תעדו הבטחות, מועדים ותוצאות במכשיר, בלי חשבון ובלי פרסומות.",
        "הבטחה,רשומה,תזכורת,דוח,החזר",
        "הבטחה של נותן שירות לא צריכה להישען על הזיכרון בלבד. Promise Guard מספק מקום מסודר לתיעוד ההבטחה ומה שקרה אחריה.",
        ["תעדו את נותן השירות, הניסוח המדויק, הערוץ, התאריכים, הסכום וההפניה", "שמרו את הרשומה המקורית והוסיפו תיקונים, עדכונים ותוצאות עם תאריך", "צרפו חומרים תומכים והגדירו תזכורות פרטיות", "ראו רשומות פתוחות, קרובות, פתורות ובארכיון", "הכינו סיכום אישי עובדתי בן עמוד אחד ובדקו אותו לפני שיתוף"],
        "מתוכנן לאחסון מקומי: אין צורך בחשבון או בשרת תוכן של GoodUse Studios. בלי פרסומות. אתם בוחרים אם לייצא, לגבות או לשתף.",
        "צרו שתי רשומות מלאות ללא תשלום. רכישה חד-פעמית בתוך היישום פותחת יצירת רשומות נוספות. הרשומות הקיימות זמינות גם ללא רכישה.",
        "צרו שתי רשומות מלאות ללא תשלום. יצירת רשומות נוספות דורשת מנוי חודשי המתחדש אוטומטית. הרשומות הקיימות זמינות גם אחרי סיום המנוי.",
        "Promise Guard אינו מאמת רשומות, קובע שהופרה הבטחה או מספק ייעוץ משפטי. הדוחות הם סיכומים אישיים המבוססים על הנתונים שלכם.",
    ),
}


# Region-sensitive wording. Copy not listed here inherits the culturally neutral
# language pack above; these overrides prevent false mechanical equivalence.
REGION_OVERRIDES = {
    "en-GB": {"short": "Record provider promises, dates and outcomes, with no account or adverts."},
    "es-ES": {"short": "Registra promesas, fechas y resultados sin cuenta ni publicidad."},
    "pt-BR": {
        "subtitle": "Promessas sempre bem claras",
        "promo": "Registre o que foi prometido, adicione datas e arquivos, acompanhe o resultado e prepare um resumo factual. Sem conta e sem anúncios.",
        "short": "Registre promessas, datas e resultados localmente, sem conta nem anúncios.",
    },
    "fr-CA": {
        "promo": "Consignez la promesse, ajoutez dates et pièces, suivez le résultat et préparez un résumé personnel factuel. Sans compte ni publicité.",
    },
}

APPLE_LOCALES = {
    "en-US": "en", "en-CA": "en", "en-GB": "en",
    "es-MX": "es", "es-ES": "es", "pt-PT": "pt", "pt-BR": "pt",
    "fr-FR": "fr", "fr-CA": "fr", "de-DE": "de", "it": "it",
    "nl-NL": "nl", "pl": "pl", "tr": "tr", "ro": "ro", "cs": "cs",
    "uk": "uk", "ru": "ru", "ar": "ar", "zh-Hans": "zh-Hans",
    "zh-Hant": "zh-Hant", "ja": "ja", "ko": "ko", "hi": "hi",
    "vi": "vi", "id": "id", "th": "th", "ms": "ms", "fi": "fi",
    "sv": "sv", "da": "da", "no": "nb", "el": "el", "he": "he",
}

GOOGLE_LOCALES = {
    "en-US": "en", "en-CA": "en", "en-GB": "en",
    "es-419": "es", "es-ES": "es", "pt-PT": "pt", "pt-BR": "pt",
    "fr-FR": "fr", "fr-CA": "fr", "de-DE": "de", "it-IT": "it",
    "nl-NL": "nl", "pl-PL": "pl", "tr-TR": "tr", "ro": "ro",
    "cs-CZ": "cs", "uk": "uk", "ru-RU": "ru", "ar": "ar",
    "zh-CN": "zh-Hans", "zh-TW": "zh-Hant", "ja-JP": "ja",
    "ko-KR": "ko", "hi-IN": "hi", "ur": "ur", "bn-BD": "bn",
    "vi": "vi", "id": "id", "th": "th", "fil": "fil", "ms-MY": "ms",
    "fi-FI": "fi", "sv-SE": "sv", "da-DK": "da", "no-NO": "nb",
    "el-GR": "el", "iw-IL": "he",
}


def pack_for(locale, language):
    result = dict(PACKS[language])
    result.update(REGION_OVERRIDES.get(locale, {}))
    return result


def description(pack, access):
    bullets = "\n".join(f"• {item}" for item in pack["features"])
    return f'{pack["intro"]}\n\n{bullets}\n\n{pack["private"]}\n\n{access}\n\n{pack["caution"]}'


def build():
    apple = {
        "product": "Promise Guard",
        "platform": "iOS",
        "urls": {"privacy_policy": PRIVACY_URL, "support": SUPPORT_URL, "marketing": MARKETING_URL},
        "locales": {},
    }
    for locale, language in APPLE_LOCALES.items():
        pack = pack_for(locale, language)
        apple["locales"][locale] = {
            "name": "Promise Guard",
            "subtitle": pack["subtitle"],
            "promotional_text": pack["promo"],
            "description": description(pack, pack["ios"]),
            "keywords": pack["keywords"],
        }

    google = {
        "product": "Promise Guard",
        "platform": "Android",
        "privacy_policy_url": PRIVACY_URL,
        "support_url": SUPPORT_URL,
        "locales": {},
    }
    for locale, language in GOOGLE_LOCALES.items():
        pack = pack_for(locale, language)
        google["locales"][locale] = {
            "app_name": "Promise Guard",
            "short_description": pack["short"],
            "full_description": description(pack, pack["android"]),
        }

    (ROOT / "app-store.json").write_text(json.dumps(apple, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "google-play.json").write_text(json.dumps(google, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
