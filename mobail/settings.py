from pathlib import Path

# 🏗️ المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# ⚙️ إعدادات الأمان
SECRET_KEY = 'django-insecure-osz5ao4b_36*=as&@zmh6a52-@aleind-duh@5xe-t6b@!b2p-'
DEBUG = True
ALLOWED_HOSTS = []

# 🧩 التطبيقات المثبتة
INSTALLED_APPS = [
    # 🔹 تطبيقات Django الافتراضية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 📦 تطبيقات المشروع المخصصة
    'store',     # 🛍️ إدارة المنتجات والعروض والتقييمات
    'accounts',  # 👤 إدارة المستخدمين والعناوين
    'orders',    # 📦 إدارة السلة والطلبات والمدفوعات
]

# 🧱 الطبقات الوسيطة (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # ✅ لدعم اللغة العربية
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🔗 روابط المشروع
ROOT_URLCONF = 'mobail.urls'

# 🧩 إعدادات القوالب (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',              # 📁 القوالب العامة
            BASE_DIR / 'store' / 'templates',    # 🛍️ قوالب المتجر
            BASE_DIR / 'accounts' / 'templates', # 👤 قوالب الحسابات
            BASE_DIR / 'orders' / 'templates',   # 📦 قوالب الطلبات
        ],
        'APP_DIRS': True,  # ✅ Django يبحث تلقائيًا داخل التطبيقات
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # مهم لخاصية {% url %}
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🚀 تطبيق WSGI
WSGI_APPLICATION = 'mobail.wsgi.application'

# 🗄️ قاعدة البيانات (SQLite مؤقتًا أثناء التطوير)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔐 التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 الإعدادات الدولية واللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'             # ✅ اللغة الافتراضية العربية
TIME_ZONE = 'Asia/Riyadh'        # ✅ التوقيت المحلي للرياض
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 📦 إعدادات الملفات الثابتة (CSS, JS, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # 📁 ملفات التطوير
STATIC_ROOT = BASE_DIR / 'staticfiles'    # 📦 لتجميع الملفات في الإنتاج

# 🖼️ إعدادات ملفات الوسائط (الصور المرفوعة)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 🔑 نوع المفتاح الافتراضي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 👤 نموذج المستخدم المخصص
AUTH_USER_MODEL = 'accounts.User'

# 📦 تفعيل عرض ملفات الوسائط أثناء التطوير (عبر urls.py)
# أضف هذا الكود في نهاية mobail/urls.py:
# ---------------------------------------
# from django.conf import settings
# from django.conf.urls.static import static
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ---------------------------------------
