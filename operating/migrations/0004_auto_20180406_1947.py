# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-06 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0003_datasetmodel_objectviewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companynetpercentage',
            name='industry',
            field=models.CharField(choices=[('Advertising', 'Advertising'), ('aerospace', 'aerospace'), ('air transport', 'air transport'), ('apparel', 'apparel'), ('Auto & Truck', 'Auto & Truck'), ('Auto Parts', 'Auto Parts'), ('Utility (Water)', 'Utility (Water)'), ('Utility (General)', 'Utility (General)'), ('Trucking', 'Trucking'), ('Transportation (Railroads)', 'Transportation (Railroads)'), ('Transportation', 'Transportation'), ('Tobacco', 'Tobacco'), ('Telecom. Services', 'Telecom. Services'), ('Telecom. Equipment', 'Telecom. Equipment'), ('Telecom (Wireless)', 'Telecom (Wireless)'), ('Steel', 'Steel'), ('Software (System & Application)', 'Software (System & Application)'), ('Software (Internet)', 'Software (Internet)'), ('Software (Entertainment)', 'Software (Entertainment)'), ('Shoe', 'Shoe'), ('Shipbuilding & Marine', 'Shipbuilding & Marine'), ('Semiconductor Equip', 'Semiconductor Equip'), ('Semiconductor', 'Semiconductor'), ('Rubber& Tires', 'Rubber& Tires'), ('Retail (Special Lines)', 'Retail (Special Lines)'), ('Retail (Online)', 'Retail (Online)'), ('Retail (Grocery and Food)', 'Retail (Grocery and Food)'), ('Retail (General)', 'Retail (General)'), ('Retail (Distributors)', 'Retail (Distributors)'), ('Retail (Building Supply)', 'Retail (Building Supply)'), ('Retail (Automotive)', 'Retail (Automotive)'), ('Restaurant/Dining', 'Restaurant/Dining'), ('Reinsurance', 'Reinsurance'), ('Recreation', 'Recreation'), ('Real Estate (Operations & Services)', 'Real Estate (Operations & Services)'), ('Real Estate (General/Diversified)', 'Real Estate (General/Diversified)'), ('Real Estate (Development)', 'Real Estate (Development)'), ('R.E.I.T.', 'R.E.I.T.'), ('Publishing & Newspapers', 'Publishing & Newspapers'), ('Precious Metals', 'Precious Metals'), ('Power', 'Power'), ('Paper/Forest Products', 'Paper/Forest Products'), ('Packaging & Container', 'Packaging & Container'), ('Oilfield Svcs/Equip.', 'Oilfield Svcs/Equip.'), ('Oil/Gas Distribution', 'Oil/Gas Distribution'), ('Oil/Gas (Production and Exploration)', 'Oil/Gas (Production and Exploration)'), ('Oil/Gas (Integrated)', 'Oil/Gas (Integrated)')], max_length=25),
        ),
        migrations.AlterField(
            model_name='trialbalance',
            name='industry',
            field=models.CharField(choices=[('Advertising', 'Advertising'), ('aerospace', 'aerospace'), ('air transport', 'air transport'), ('apparel', 'apparel'), ('Auto & Truck', 'Auto & Truck'), ('Auto Parts', 'Auto Parts'), ('Utility (Water)', 'Utility (Water)'), ('Utility (General)', 'Utility (General)'), ('Trucking', 'Trucking'), ('Transportation (Railroads)', 'Transportation (Railroads)'), ('Transportation', 'Transportation'), ('Tobacco', 'Tobacco'), ('Telecom. Services', 'Telecom. Services'), ('Telecom. Equipment', 'Telecom. Equipment'), ('Telecom (Wireless)', 'Telecom (Wireless)'), ('Steel', 'Steel'), ('Software (System & Application)', 'Software (System & Application)'), ('Software (Internet)', 'Software (Internet)'), ('Software (Entertainment)', 'Software (Entertainment)'), ('Shoe', 'Shoe'), ('Shipbuilding & Marine', 'Shipbuilding & Marine'), ('Semiconductor Equip', 'Semiconductor Equip'), ('Semiconductor', 'Semiconductor'), ('Rubber& Tires', 'Rubber& Tires'), ('Retail (Special Lines)', 'Retail (Special Lines)'), ('Retail (Online)', 'Retail (Online)'), ('Retail (Grocery and Food)', 'Retail (Grocery and Food)'), ('Retail (General)', 'Retail (General)'), ('Retail (Distributors)', 'Retail (Distributors)'), ('Retail (Building Supply)', 'Retail (Building Supply)'), ('Retail (Automotive)', 'Retail (Automotive)'), ('Restaurant/Dining', 'Restaurant/Dining'), ('Reinsurance', 'Reinsurance'), ('Recreation', 'Recreation'), ('Real Estate (Operations & Services)', 'Real Estate (Operations & Services)'), ('Real Estate (General/Diversified)', 'Real Estate (General/Diversified)'), ('Real Estate (Development)', 'Real Estate (Development)'), ('R.E.I.T.', 'R.E.I.T.'), ('Publishing & Newspapers', 'Publishing & Newspapers'), ('Precious Metals', 'Precious Metals'), ('Power', 'Power'), ('Paper/Forest Products', 'Paper/Forest Products'), ('Packaging & Container', 'Packaging & Container'), ('Oilfield Svcs/Equip.', 'Oilfield Svcs/Equip.'), ('Oil/Gas Distribution', 'Oil/Gas Distribution'), ('Oil/Gas (Production and Exploration)', 'Oil/Gas (Production and Exploration)'), ('Oil/Gas (Integrated)', 'Oil/Gas (Integrated)')], default=0, max_length=25),
        ),
    ]
