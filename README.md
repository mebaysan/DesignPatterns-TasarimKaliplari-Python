- [Giriş](#giriş)
- [Tasarım Kalıbı Nedir?](#tasarım-kalıbı-nedir)
- [Tasarım Kalıbı Türleri Nelerdir?](#tasarım-kalıbı-türleri-nelerdir)
  - [Creational Patterns](#creational-patterns)
  - [Structural Patterns](#structural-patterns)
  - [Behavioral Patterns](#behavioral-patterns)
- [Popüler Tasarım Kalıpları](#popüler-tasarım-kalıpları)
  - [Creational Patterns](#creational-patterns-1)
    - [Singleton](#singleton)
    - [Factory Method Pattern](#factory-method-pattern)
  - [Structural Patterns](#structural-patterns-1)
    - [Facade Pattern](#facade-pattern)
    - [Adapter Pattern](#adapter-pattern)
    - [Composite Pattern](#composite-pattern)
    - [Proxy Pattern](#proxy-pattern)
    - [Decorator Pattern](#decorator-pattern)
  - [Behavioral Pattern](#behavioral-pattern)
    - [Template Method Pattern](#template-method-pattern)
    - [Chain of Responsibility Pattern](#chain-of-responsibility-pattern)
    - [State Pattern](#state-pattern)

# Giriş

Bir proje için girdiğim görüşmede CTO'dan yediğim bir tokat ile "Yazılım Mimarisi ve Tasarımı", "Yazılım Geliştirme Yaşam Döngüsü" ve "Yazılım Ürün Yönetimi" gibi konularda eksik olduğumu fark ederek bu alanlardaki eksiklerimi gidermek için hazırlıklara başladım. Eksiklerimi gidermek için ana 2 kurs olarak aşağıdaki kursları takip etme kararı aldım.
- [Software Design and Architecture Specialization](https://www.coursera.org/specializations/software-design-architecture?)
- [Software Product Management Specialization](https://www.coursera.org/specializations/product-management)

Bu dokümanda da "Yazılım Tasarımı ve Mimarisi" konusunda öğrendiklerimi paylaşmaya çalışacağım. Paylaşmayı ön gördüğüm konular aşağıdaki gibidir.
- Tasarım Kalıbı Nedir?
- Tasarım Kalıbı Türleri Nelerdir?
- Popüler Tasarım Kalıpları

# Tasarım Kalıbı Nedir?

Tasarım Kalıbı tekrar eden tasarım sorunlarına sunulmuş olan kalıcı çözümlerdir. Bu kalıplar yazılım geliştiricilerin uzun yıllardır üzerinde çalıştıkları problemleri kalıcı olarak çözmek için geliştirip üzerinde mutabık oldukları çözümlerdir. Tasarım kalıplarını kullanarak daha önceden belirlenmiş/çözülmüş olan sorunları daha rahat çözebiliriz.

# Tasarım Kalıbı Türleri Nelerdir?

Temelde 3 tip tasarım kalıbı vardır.
- Creational Patterns
- Structural Patterns
- Behavioral Patterns


## Creational Patterns

**Creational Patterns** daha çok nesneleri nasıl oluşturduğumuz ve kopyaladığımız gibi konularla (problemlerle) ilgilenir. Örnek olarak; yeni bir obje (instance) oluşturmak yerine mevcut olan objeyi kopyalamak.

## Structural Patterns

**Structural Patterns** objelerin birbirleri ile olan ilişkilerini açıklamak için kullanılır. Aynı zamanda bu kalıplar yazılım geliştirmede çok önemli iki prensip ile de ilgilidirler: **decomposition** ve **generalization**.

## Behavioral Patterns

**Behavioral Patterns** objelerin iş dağılımına odaklanmaktadır. Bağımsız objelerin ortak bir amaç uğrunda çalışmaları için karşılaşılan problemleri çözmektedir.

# Popüler Tasarım Kalıpları

## Creational Patterns

### Singleton

**Singleton** bir **"creational pattern"** dir. Tasarım kalıplarının en basit örneklerinden olmasına rağmen çok güçlü bir tekniktir. Kısaca bir sınıfı sadece bir obje sahibi olmak ile kısıtlamaktır diyebiliriz. Python örneğine bakmak için buradaki [singleton.py](src/creatorial-patterns/singleton/singleton.py) dosyasına bakabilirsiniz.

### Factory Method Pattern

**Factory Method Pattern** bir **"creational pattern"** dir. Aslında Factory Method Pattern tek başına bir kalıp değildir. Bu kalıp objeleri oluşturmak için bir `Factory` sınıfı kullanmaz. Bunun yerine sınıfın altında ayrı bir **factory method** kullanır. Bu kalıbın gücü özelleştirilmiş objeleri oluşturabilmesinden gelmektedir. Python örneğine bakmak için buradaki [factory_method.py](src/creatorial-patterns/factory-method/factory_method.py) dosyasına bakabilirsiniz.

## Structural Patterns

### Facade Pattern

İstemci (client) sınıfları ile alt sistem (subsystem) sınıfları arasındaki etkileşim için kullanılır. Facade bir `wrapper class` tır. Alt sistem sınıflarını encapsulate edip onların karmaşıklığını (complexity) gizlemek için kullanılır. İstemcilerin, alt sistem sınıfları ile `Facade` üzerinden etkileşime geçmesini sağlar. [facade.py](./src/structural-patterns/facade-pattern/facade.py) dosyasında Python ile bir örneğini bulabilirsiniz.

### Adapter Pattern

Adapter tasarım kalıbı iki farklı sistem arasında uyumlu bir arayüz (interface) görevi görür ve bu iki sistemin haberleşmesini sağlar. Adapter tasarım kalıbı birkaç parçadan oluşmaktadır.

- Bir istemci (client) sınıfı. Bu sınıf; sistemimizde üçüncü parti veya dışarıdan bir sistemi kullanmak isteyen bir parçadır. 
- Bir adaptee sınıfı. Bu üçüncü parti bir kütüphane veya dışarıdan bir servis tarafından kullanılacak olan sınıftır.
- Bir adaptör (adapter) sınıfı. Bu sınıf istemci ve adaptee sınıfları arasında bulunacaktır. Adaptör sınıfı istemcinin görmek istediği bilgiyi (data) hedef arayüzü (interface) kullanarak sağlar. Aynı zamanda istemcinin istediğini adaptee sınıfının anlayacağı şekilde çevirir (translate) ve adaptee sınıfına döner (return). Bir tür sarmalayıcı (wrapper) sınıftır.
- Bir hedef arayüz (interface). Bu da istemci tarafında isteklerini adaptör sınıfa göndermek için kullanılır.

Adapter tasarım kalıbını uygulamak için aşağıdaki adımları izleyebiliriz.

- Hedef arayüz (target interface) tasarlanır
- Hedef arayüz, adaptör sınıfına uygulanır (implement)
- İstemci (client) tarafından hedef arayüz kullanılarak istekler adaptör (adapter) sınıfa iletilir

Adapter tasarım kalıbının Python uygulamalı örneğini [adapter.py](src/structural-patterns/adapter-pattern/adapter.py) dosyasında inceleyebilirsiniz.

### Composite Pattern

Bu tasarım kalıbının ana iki hedefi vardır:

- Nesnelerin iç içe yapılarını oluşturmak için (ağaç)
- Bu nesnelerin sınıflarıyla tekdüze bir şekilde ilgilenmek

Polymorphism kullanarak, tüm sınıflar aynı arayüze (interface) uyarlar. 

Bir **Composite Class** kendisini implement eden tüm sınıfları (leaf class) tekdüze bir kalıba sokar. 

**Leaf Class** composite olmayan (non-composite) sınıfları temsil eder.

Composite Pattern, her sınıf için ağaç yapısını oluştururken bizi Polymorphism'e yönlendirirken bir arayüz (interface) implement etmeyi dayatır.

Özyinelemeli (recursive) composite adı verilen bir teknik kullanarak nesnelerin diğer nesnelerden oluşmasına izin verir.

Python'da Composite Pattern örneği için [composite.py](src/structural-patterns/composite-pattern/composite.py) dosyasına bakabilirsiniz.

### Proxy Pattern

Bu kalıp gerçek "konu/durum" (subject) sınıfını temsil eden bir **proxy** arayüzünün (interface) implement edilmesi üzerinedir. Proxy bir objenin daha basitleştirilmiş, hafif versiyonu olarak davranır. Bir Proxy obje aynı işleri orjinal obje olarak görebilir. Bunları yaparken gelen istekleri orjinal objeye delege edebilir.

Bu tasarım kalıbında proxy sınıfı gerçek konu/durum (subject) sınıfını sarmalar. Sarmalayıcı bir sınıf olarak, istemci sınıfları direkt olarak konu/durum sınıfı yerine proxy sınıf ile muhatap olurlar. Proxy sınıflarının çoğunlukla kullanıldığı üç durum:

- **Sanal (virtual) proxy** olarak davranırlar. Bu, bir proxy sınıfı olduğunda olan gerçek bir konu sınıfının yerine kullanılır. Genellikle web sayfalarındaki resimlerde veya grafik editörlerinde, yüksek çözünürlükteki resimler yüklenemeyecek kadar büyük olduğunda kullanılırlar.
- **Koruyucu (protection) proxy** olarak davranırlar. Mesela proxy sınıfın gerçek sınıfa erişimi kontrol ettiği senaryolar. Örnek olarak öğrencier ve öğretmenler tarafından kullanılan bir sistemi rollere göre kısıtlamak.
- **Uzak (remote) proxy** olarak davranırlar. Bu şekilde davranmak için proxy sınıfının localde, gerçek sınıfın uzakta (remote) var olması gereklidir. Google Docs, web tarayıcılarının yerel olarak ihtiyaç duyduğu tüm nesnelere sahip olan fakat başka bir yerde Google sunucusunda bulunan kaynaklar için bundan yararlanır.

Proxy kalıbının Python ile örneği [proxy.py](src/structural-patterns/proxy-pattern/proxy.py) dosyasında gösterilmiştir.

### Decorator Pattern

Çeşitli davranışları esnekçe uygulayabilmemizi sağlayan bir tasarım kalıbıdır. Ancak, bir nesnenin davranışı sınıfı tarafından tanımlandığından ve yalnızca derleme zamanında gerçekleştiğinden, bir program çalışırken sınıflarda değişiklik yapılamaz. Ek davranışsal özellikleri veya sorumlulukları dinamik olarak bir objeye toplulaştırma (aggregation) kullanarak çalışma esnasında atar.

Proxy kalıbının Python ile örneği [decorator.py](src/structural-patterns/decorator-pattern/decorator.py) dosyasında gösterilmiştir.


## Behavioral Pattern

### Template Method Pattern

Template Method kalıbı, ana sınıftan alt sınıfa implement ederek bir algoritmanın adımlarını tanımlar. 

Bu kalıbın kullanılabileceği en iyi senaryolardan biri iki sınıfı tek bir ana sınıfta (superclass) genellemeye (generalize) çalışmaktır. Çok benzer işlevselliğe ve işlem sırasına sahip iki ayrı sınıfımız olduğunda kullanabileceğimiz bir tekniktir. Bir template method kullanmayı seçebiliriz, bu nedenle bu algoritmalarda yapılan değişikliklerin iki yerine yalnızca bir yerde uygulanması gerekir.

Template Method kalıbının Python ile örneği [template_method.py](src/behavioral-patterns/template-method-pattern/template_method.py) dosyasında gösterilmiştir. 

### Chain of Responsibility Pattern

Chain of Responsibility kalıbı, isteklerin işlenmesinden sorumlu olan bir nesneler zinciridir. Yazılım tasarımında bu nesneler birbirine bağlı işleyici nesnelerdir.

Aralardaki her filtre aşağıdaki adımları uygulamalıdır:

- Kuralın eşleşip eşleşmediğini kontrol et
- Eğer eşleşiyorsa, uygulaman gereken fonksiyonu uygula (ör: mail at, sayfaya yönlendir vs.)
- Eğer eşleşmiyorsa, sıradaki diğer filtreyi çağır


Chain of Responsibility kalıbının Python ile örneği [chain_responsibility.py](src/behavioral-patterns/chain-of-responsibility/chain_responsibility.py) dosyasında gösterilmiştir.

### State Pattern

Kodumuzdaki nesneler mevcut durumlarının farkındadır. Mevcut durumlarına göre uygun bir davranış seçebilirler. Mevcut durumları değiştiğinde, bu davranış değiştirilebilir. Bu State Pattern kalıbıdır.

State Pattern kalıbının Python ile örneği [state.py](state.src/behavioral-patterns/state-pattern/state.py) dosyasında gösterilmiştir.