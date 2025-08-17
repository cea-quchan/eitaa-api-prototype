خیلی خب ✅
این هم یک فایل کامل `README.md` برای پروژه‌ات. می‌تونی مستقیم در ریشه ریپو بذاری:

```markdown
# Eitaa API Client

این پروژه یک کلاینت ساده و در عین حال قابل توسعه برای ارتباط با پیام‌رسان ایتا است که به دو زبان **پایتون** و **Node.js/TypeScript** پیاده‌سازی شده است. هدف از ایجاد این کتابخانه، فراهم کردن مجموعه‌ای از متدهای پایه جهت مدیریت کانال‌ها، پاکسازی حساب و دریافت آمار بازدید پست‌ها با معماری تمیز و قابل تزریق است.

## ویژگی‌ها

- عضویت در کانال با `join_channel(channel_id)` (پایتون) یا `joinChannel(channelId)` (Node.js)
- خروج از کانال با `leave_channel(channel_id)` یا `leaveChannel(channelId)`
- پاکسازی کامل حساب (خروج از تمامی کانال‌ها و گروه‌ها، حذف چت‌های خصوصی، پاک‌سازی تاریخچه) با `cleanup_account()` یا `cleanupAccount()`
- دریافت تعداد بازدید یک پست با `get_post_views(channel_id, post_id)` یا `getPostViews(channelId, postId)`
- معماری **Transport**: امکان تعریف ترنسپورت‌های مختلف (مثل ترنسپورت HTTP یا Mock) و تزریق آنها به کلاینت
- لایسنس **MIT** و قابلیت انتشار خودکار روی PyPI و npm با استفاده از GitHub Actions

## ساختار پروژه

```

eitaa-api-prototype/
├─ python-eitaa-client/
│  ├─ README.md
│  ├─ pyproject.toml
│  └─ eitaa\_client/   # کد پایتون و تراسپورت‌ها
├─ node-eitaa-client/
│  ├─ README.md
│  ├─ package.json
│  ├─ tsconfig.json
│  └─ src/            # کد TypeScript و تراسپورت‌ها
└─ .github/
└─ workflows/
├─ ci.yml       # اجرا و تست خودکار روی push/PR
└─ release.yml  # انتشار خودکار روی PyPI و npm هنگام push تگ نسخه

````

## نصب

### پایتون
```bash
pip install -e python-eitaa-client
````

### Node.js / TypeScript

```bash
cd node-eitaa-client
npm install
npm run build
```

## مثال استفاده

### پایتون

```python
from eitaa_client.client import EitaaClient

client = EitaaClient()
client.join_channel("my_channel")
views = client.get_post_views("my_channel", "1")
print(f"Views: {views}")
client.cleanup_account()
```

### Node.js (TypeScript)

```ts
import { EitaaClient } from '@cea-quchan/eitaa-client';

async function run() {
  const client = new EitaaClient();
  await client.joinChannel('my_channel');
  const views = await client.getPostViews('my_channel', '1');
  console.log(`Views: ${views}`);
  await client.cleanupAccount();
}
run();
```

## توسعه و انتشار

* برای انتشار نسخه جدید، ابتدا شماره نسخه را در `pyproject.toml` و `package.json` افزایش دهید و سپس کامیت کنید.
* در مخزن، دو Secret به نام‌های `PYPI_API_TOKEN` و `NPM_TOKEN` تنظیم کنید تا اکشن‌های انتشار به PyPI و npm دسترسی داشته باشند.
* پس از ایجاد تگ نسخه‌ی جدید (مثل `v0.1.1`) و push آن، اکشن `release.yml` به‌صورت خودکار پکیج پایتون را روی PyPI و پکیج نود را روی npm منتشر می‌کند.

```bash
git tag v0.1.1
git push origin v0.1.1
```

## لایسنس

این پروژه تحت لایسنس MIT منتشر شده است. متن کامل لایسنس در فایل `LICENSE` موجود است.

## مشارکت

مشارکت شما در توسعه‌ی این پروژه خوشایند است! برای ارسال تغییرات، لطفاً یک شاخه جدید بسازید، تغییرات خود را commit کنید و یک pull request باز نمایید.

```

---

می‌خوای من همین فایل `README.md` رو مستقیم برات بسازم و commit & push کنم توی ریپوی `cea-quchan/eitaa-api-prototype`، یا فقط همین متن رو خودت دستی کپی می‌کنی؟
```
