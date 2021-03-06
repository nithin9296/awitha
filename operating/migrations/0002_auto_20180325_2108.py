# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-25 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='trialbalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default=0, max_length=25)),
                ('region', models.CharField(choices=[('United States', 'United States'), ('Aus, NZ & Canada', 'Aus, NZ & Canada'), ('Europe', 'Europe'), ('Emerging Markets', 'Emerging Markets'), ('Japan', 'Japan')], default=0, max_length=25)),
                ('industry', models.CharField(choices=[('Advertising', 'Advertising'), ('aerospace', 'aerospace'), ('air transport', 'air transport'), ('apparel', 'apparel'), ('Auto & Truck', 'Auto & Truck'), ('Auto Parts', 'Auto Parts'), ('Utility (Water)', 'Utility (Water)'), ('Utility (General)', 'Utility (General)'), ('Trucking', 'Trucking'), ('Transportation (Railroads)', 'Transportation (Railroads)'), ('Transportation', 'Transportation'), ('Tobacco', 'Tobacco'), ('Telecom. Services', 'Telecom. Services'), ('Telecom. Equipment', 'Telecom. Equipment'), ('Telecom (Wireless)', 'Telecom (Wireless)'), ('Steel', 'Steel'), ('Software (System & Application)', 'Software (System & Application)'), ('Software (Internet)', 'Software (Internet)'), ('Software (Entertainment)', 'Software (Entertainment)'), ('Shoe', 'Shoe'), ('Shipbuilding & Marine', 'Shipbuilding & Marine'), ('Semiconductor Equip', 'Semiconductor Equip'), ('Semiconductor', 'Semiconductor'), ('Rubber& Tires', 'Rubber& Tires'), ('Retail (Special Lines)', 'Retail (Special Lines)'), ('Retail (Online)', 'Retail (Online)'), ('Retail (Grocery and Food)', 'Retail (Grocery and Food)'), ('Retail (General)', 'Retail (General)'), ('Retail (Distributors)', 'Retail (Distributors)'), ('Retail (Building Supply)', 'Retail (Building Supply)'), ('Retail (Automotive)', 'Retail (Automotive)'), ('Restaurant/Dining', 'Restaurant/Dining'), ('Reinsurance', 'Reinsurance'), ('Recreation', 'Recreation'), ('Real Estate (Operations & Services)', 'Real Estate (Operations & Services)'), ('Real Estate (General/Diversified)', 'Real Estate (General/Diversified)'), ('Real Estate (Development)', 'Real Estate (Development)'), ('R.E.I.T.', 'R.E.I.T.'), ('Publishing & Newspapers', 'Publishing & Newspapers'), ('Precious Metals', 'Precious Metals'), ('Power', 'Power'), ('Paper/Forest Products', 'Paper/Forest Products'), ('Packaging & Container', 'Packaging & Container')], default=0, max_length=25)),
                ('glcode', models.IntegerField(default=0)),
                ('gldescription', models.CharField(max_length=60)),
                ('classification', models.CharField(max_length=30)),
                ('subclassification', models.CharField(max_length=30)),
                ('debit_2017', models.IntegerField(default=0)),
                ('credit_2017', models.IntegerField(default=0)),
                ('debit_2016', models.IntegerField(default=0)),
                ('credit_2016', models.IntegerField(default=0)),
                ('debit_2015', models.IntegerField(default=0)),
                ('credit_2015', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.RemoveField(
            model_name='operatingmargin',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='operatingmargin',
            name='region',
        ),
        migrations.RemoveField(
            model_name='companynetpercentage',
            name='npy2015',
        ),
        migrations.RemoveField(
            model_name='companynetpercentage',
            name='npy2016',
        ),
        migrations.RemoveField(
            model_name='companynetpercentage',
            name='npy2017',
        ),
        migrations.RemoveField(
            model_name='npmargin',
            name='npy2015',
        ),
        migrations.RemoveField(
            model_name='npmargin',
            name='npy2016',
        ),
        migrations.RemoveField(
            model_name='npmargin',
            name='npy2017',
        ),
        migrations.AddField(
            model_name='companynetpercentage',
            name='debtequity_ratio_2015',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='companynetpercentage',
            name='debtequity_ratio_2016',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='companynetpercentage',
            name='debtequity_ratio_2017',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='companynetpercentage',
            name='gross_profit_margin_2015',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='companynetpercentage',
            name='gross_profit_margin_2016',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='companynetpercentage',
            name='gross_profit_margin_2017',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='companynetpercentage',
            name='netmargin_percentage_2015',
            field=models.DecimalField(decimal_places=2, default=4, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companynetpercentage',
            name='netmargin_percentage_2016',
            field=models.DecimalField(decimal_places=2, default=4, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companynetpercentage',
            name='netmargin_percentage_2017',
            field=models.DecimalField(decimal_places=2, default=4, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companynetpercentage',
            name='user',
            field=models.CharField(default=4, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='npmargin',
            name='debtequity_ratio_2015',
            field=models.DecimalField(decimal_places=2, default=4, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='npmargin',
            name='debtequity_ratio_2016',
            field=models.DecimalField(decimal_places=2, default=4, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='npmargin',
            name='debtequity_ratio_2017',
            field=models.DecimalField(decimal_places=2, default=4, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='npmargin',
            name='gross_profit_margin_2015',
            field=models.DecimalField(decimal_places=2, default=4, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='npmargin',
            name='gross_profit_margin_2016',
            field=models.DecimalField(decimal_places=2, default=4, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='npmargin',
            name='gross_profit_margin_2017',
            field=models.DecimalField(decimal_places=2, default=4, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='npmargin',
            name='netmargin_percentage_2015',
            field=models.DecimalField(decimal_places=2, default=4, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='npmargin',
            name='netmargin_percentage_2016',
            field=models.DecimalField(decimal_places=2, default=4, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='npmargin',
            name='netmargin_percentage_2017',
            field=models.DecimalField(decimal_places=2, default=4, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companynetpercentage',
            name='industry',
            field=models.CharField(choices=[('Advertising', 'Advertising'), ('aerospace', 'aerospace'), ('air transport', 'air transport'), ('apparel', 'apparel'), ('Auto & Truck', 'Auto & Truck'), ('Auto Parts', 'Auto Parts'), ('Utility (Water)', 'Utility (Water)'), ('Utility (General)', 'Utility (General)'), ('Trucking', 'Trucking'), ('Transportation (Railroads)', 'Transportation (Railroads)'), ('Transportation', 'Transportation'), ('Tobacco', 'Tobacco'), ('Telecom. Services', 'Telecom. Services'), ('Telecom. Equipment', 'Telecom. Equipment'), ('Telecom (Wireless)', 'Telecom (Wireless)'), ('Steel', 'Steel'), ('Software (System & Application)', 'Software (System & Application)'), ('Software (Internet)', 'Software (Internet)'), ('Software (Entertainment)', 'Software (Entertainment)'), ('Shoe', 'Shoe'), ('Shipbuilding & Marine', 'Shipbuilding & Marine'), ('Semiconductor Equip', 'Semiconductor Equip'), ('Semiconductor', 'Semiconductor'), ('Rubber& Tires', 'Rubber& Tires'), ('Retail (Special Lines)', 'Retail (Special Lines)'), ('Retail (Online)', 'Retail (Online)'), ('Retail (Grocery and Food)', 'Retail (Grocery and Food)'), ('Retail (General)', 'Retail (General)'), ('Retail (Distributors)', 'Retail (Distributors)'), ('Retail (Building Supply)', 'Retail (Building Supply)'), ('Retail (Automotive)', 'Retail (Automotive)'), ('Restaurant/Dining', 'Restaurant/Dining'), ('Reinsurance', 'Reinsurance'), ('Recreation', 'Recreation'), ('Real Estate (Operations & Services)', 'Real Estate (Operations & Services)'), ('Real Estate (General/Diversified)', 'Real Estate (General/Diversified)'), ('Real Estate (Development)', 'Real Estate (Development)'), ('R.E.I.T.', 'R.E.I.T.'), ('Publishing & Newspapers', 'Publishing & Newspapers'), ('Precious Metals', 'Precious Metals'), ('Power', 'Power'), ('Paper/Forest Products', 'Paper/Forest Products'), ('Packaging & Container', 'Packaging & Container')], max_length=25),
        ),
        migrations.DeleteModel(
            name='operatingmargin',
        ),
    ]
