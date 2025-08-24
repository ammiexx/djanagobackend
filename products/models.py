from django.db import models
from cloudinary.models import CloudinaryField
class Product(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_photo=CloudinaryField('image',null=True,blank=True)
    product_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    product_photo = CloudinaryField('image',null=True,blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(
        max_length=50,
        choices=[('fashions', 'Fashions'), ('electronics', 'Electronics'),('homes', 'Homes'),('carbrands', 'Car Brands'),
                 ('foods', 'Foods & Beverages'),('appliances', 'Home & Appliances'),('health', 'Health & Beauties'),
                 ('events', 'Events & Weddings'),('entertainments', 'Intertainments'),('travels', 'Travels'),
                 ('daily', 'Daily Discounts'),('weekly', 'Weekly Discounts'),('new', 'New Advantages'),
                 ('newoffers', 'New Offers'),('upcomming', 'Upcomming Services'),('repair', 'Repair & Maintainance'),
                 ('agricultural', 'Agriculture & Livestock'),('books', 'Books & Stationary'),('toys', 'Toys & Games'),('jewelry', 'Jewelries'),
                 ('insurances', 'Finance & Insurances'),('baby', 'Baby & Kids products'),('pet', 'Pet Suplies & services'),('green', 'Green & Eco-friendly products'),
                 ('medical', 'Medical & Pharmaceuticals'),('logistic', 'logistic & Delivery Services'),('consultancy', 'Legal & Consultancy Services'),('cleaning', 'Cleaning & Sanitation Services'),
                 ('telecom', 'Telecomunication Services'),('art', 'Art & Handicrafts'),('photograpy', 'Photograpy & Videograph'),('design', 'Furniture & Interior Design'),
                 ('fitness', 'Fitness & Sports Service'),('software', 'Software & IT services'),('sercurity', 'Security Services'),('printing', 'Printing & publishing'),
                 ('automotive', 'Automotive Services'),('waste', 'Waste Management & Recycling '),('human', 'Human Resources & staffing'),('energy', 'Energy & Utilities'),
                 ('gaming', 'Gaming & eSports'),('tatue', 'Tatto And Piercing Studios'),('nursing', 'Elderly Care & Nursing Services'),('rental', 'Rental Services'),
                 ('decor', 'Event Planning & Decor'),('translation', 'Language And Translation'),('nonprofit', 'Non Profit & Charity Organization'),('freight', 'Courier & Freight Services'),
                 ('sallons', 'Beauty Sallons and Barbershops'),('music', 'Music & Instruments'),('office', 'Coworking & Office Spaces'),('digital', 'Digital Marketing Services'),
                 ('architecture', 'Architecture & Engineering Services'),('mental', 'Mental Health & Wellness Services'),('homesecurity', 'Home Securty & Smart Homes'),('land', 'Land Escaping and Gardeing services'),
                 ('podcasting', 'podcasting & Audio Production'),('stationary', 'Stationary & Office Supplieis'),('marin', 'Marine & boating Services'),('virtual', 'Virtual Events and Webinars'),
                 ('funding', 'Croud Funding And Investment Services'),('elearning', 'Elearning & online Cources'),('carwash', 'Car Wash & Detailing'),('admin', 'Virtual Assistant & Admin Support'),
                 ],
        null=True,
        blank=True
    )
    condition = models.CharField(
        max_length=50,
        choices=[('new', 'New'), ('used', 'Used')],
        null=True,
        blank=True
    )
    location = models.CharField(max_length=255, null=True, blank=True)
    contact_telegram = models.URLField(blank=True, null=True)
    contact_tick = models.URLField(blank=True, null=True)
    web_site = models.URLField(blank=True, null=True)
    contact_phone = models.CharField(max_length=30, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.product_name
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('pimages',null=True,blank=True)
    def __str__(self):
        return f"Image for {self.product.product_name}"
