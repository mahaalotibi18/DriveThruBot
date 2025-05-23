def اختيار_اللغة():
    print("اختر اللغة:")
    print("1. العربية")
    print("2. English")
    اختيار = input(">> ")

    if اختيار == "1" or "عربي" in اختيار:
        return "ar"
    elif اختيار == "2" or "english" in اختيار.lower():
        return "en"
    else:
        print("خيار غير معروف، سيتم اختيار العربية تلقائياً.")
        return "ar"

def عرض_المنيو():
    print("\nقائمة المنتجات:")
    print("1. كوفي اليوم - 4 ريال")
    print("2. أمريكانو - 5 ريال")
    print("3. لاتيه - 6 ريال")
    print("4. كابتشينو - 6 ريال")

def احصل_على_السعر(المشروب):
    الأسعار = {
        "كوفي اليوم": 4,
        "أمريكانو": 5,
        "لاتيه": 6,
        "كابتشينو": 6
    }
    return الأسعار.get(المشروب, 0)

def اختيار_المشروب():
    المشروب = input("اختر مشروبك من القائمة >> ")
    return المشروب

def حار_او_بارد():
    print("هل تريده حار أم بارد؟")
    خيار = input(">> ")
    return خيار

def سكر_او_بدون():
    print("هل تريده بسكر أم بدون سكر؟")
    خيار = input(">> ")
    return خيار

def إضافات_القهوة(المشروب):
    if "كوفي" in المشروب or "أمريكانو" in المشروب.lower():
        print("اختر نوع البن:")
        print("1. برازيلي")
        print("2. إثيوبي")
        print("3. كولومبي")
        خيار = input(">> ")
        return خيار
    else:
        return "لا توجد إضافات مخصصة لهذا المشروب."

def الحجم():
    print("اختر الحجم:")
    print("1. صغير")
    print("2. وسط")
    print("3. كبير")
    خيار = input(">> ")
    return خيار

def بدء_الطلب():
    اللغة = اختيار_اللغة()

    if اللغة == "ar":
        while True:
            print("\nمرحباً بك!")
            عرض_المنيو()
            المشروب = اختيار_المشروب()
            حرارة = حار_او_بارد()
            سكر = سكر_او_بدون()
            الإضافة = إضافات_القهوة(المشروب)
            الحجم_المختار = الحجم()
            السعر = احصل_على_السعر(المشروب)

            print("\n-- ملخص الطلب --")
            print(f"المشروب: {المشروب}")
            print(f"الحرارة: {حرارة}")
            print(f"السكر: {سكر}")
            print(f"الإضافات: {الإضافة}")
            print(f"الحجم: {الحجم_المختار}")
            print(f"السعر: {السعر} ريال")

            print("\nهل هذا صحيح؟ (نعم / لا)")
            تأكيد = input(">> ")

            if "لا" in تأكيد or "no" in تأكيد.lower():
                print("\nحسناً، دعنا نعيد الطلب من جديد...\n")
                continue
            else:
                print("\nحسناً، نتمنى لك يوماً سعيداً! تفضل إلى الأمام.")
                break

# تشغيل البرنامج
بدء_الطلب()