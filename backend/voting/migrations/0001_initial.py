from django.db import migrations, models
import django.db.models.deletion

def candidate_upload_path(instance, filename):
    return f"candidates/{instance.slug or 'candidate'}/{filename}"

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('price_per_vote', models.PositiveIntegerField(default=100)),
                ('currency', models.CharField(default='XAF', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=120)),
                ('short_description', models.CharField(blank=True, max_length=200)),
                ('bio', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='candidates/candidate/')),
                ('photo_url', models.URLField(blank=True)),
                ('slug', models.SlugField(blank=True, max_length=140, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('votes_count', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voting.category')),
            ],
        ),
        migrations.CreateModel(
            name='VoteIntent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes_requested', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('payment_ref', models.CharField(max_length=64, unique=True)),
                ('status', models.CharField(choices=[('PENDING','PENDING'),('PAID','PAID'),('FAILED','FAILED'),('EXPIRED','EXPIRED')], default='PENDING', max_length=10)),
                ('payer_phone', models.CharField(max_length=20)),
                ('provider', models.CharField(choices=[('MTN','MTN'),('ORANGE','ORANGE')], max_length=10)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('user_agent', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voting.campaign')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voting.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voting.campaign')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voting.candidate')),
                ('vote_intent', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='voting.voteintent')),
            ],
        ),
    ]
