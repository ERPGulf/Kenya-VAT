## KENYA VAT management APP - ERPNext module

Specific app for the region Kenya to generate QR Code on submitting `Sales Invoice`

You can install the app from https://github.com/ERPGulf/kenya_vat.git

Please send us your suggestions and feedback to support@erpgulf.com

Please visit our website www.erpgulf.com and our hosting provider www.claudion.com ( Claudion provides VMs, cloud servers, email and web hostings for Gulf companies. hosted in Jeddah, Dubai and Doha. Provides fastest hosting service in your own city. )


How to install
--------------

> NOTE : This documentation assumes you are in bench directory.To confirm type `bench find .`

```
bench get-app kenya_vat https://github.com/ERPGulf/kenya_vat.git

bench --site "YOUR_SITE_NAME"  install-app kenya_vat

bench --site "YOUR_SITE_NAME" migrate 
```

*To confirm installation,Go to `Help > About`. You can see all installed apps.If the app is not listed in there, clear the cache and reload*

If you face any issue with installation, send email to support@ERPGulf.com.

Once you have installed the app, you can create a sample invoice in `Sales Invoice` and submit the invoice. You can see the Generated QR Code.

![kenya-qr-code](https://user-images.githubusercontent.com/48277875/190914414-62629a34-4893-47d6-bb1b-702976906160.jpg)

#### License

MIT
