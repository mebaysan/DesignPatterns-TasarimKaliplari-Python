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

