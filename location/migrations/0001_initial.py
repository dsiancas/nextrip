# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'location_location', (
            ('id_location', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=650)),
        ))
        db.send_create_signal(u'location', ['Location'])

        # Adding model 'Hotel'
        db.create_table(u'location_hotel', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('id_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['location.Location'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=650)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'location', ['Hotel'])

        # Adding model 'Restaurant'
        db.create_table(u'location_restaurant', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('id_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['location.Location'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=650)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'location', ['Restaurant'])

        # Adding model 'General'
        db.create_table(u'location_general', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('id_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['location.Location'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=650)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=650)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=650)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=650)),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=650)),
            ('visaReq', self.gf('django.db.models.fields.BooleanField')(max_length=650)),
        ))
        db.send_create_signal(u'location', ['General'])

        # Adding model 'Sport'
        db.create_table(u'location_sport', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('id_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['location.Location'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=650)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=650)),
        ))
        db.send_create_signal(u'location', ['Sport'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'location_location')

        # Deleting model 'Hotel'
        db.delete_table(u'location_hotel')

        # Deleting model 'Restaurant'
        db.delete_table(u'location_restaurant')

        # Deleting model 'General'
        db.delete_table(u'location_general')

        # Deleting model 'Sport'
        db.delete_table(u'location_sport')


    models = {
        u'location.general': {
            'Meta': {'object_name': 'General'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '650'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '650'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '650'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'id_location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['location.Location']"}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '650'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '650'}),
            'visaReq': ('django.db.models.fields.BooleanField', [], {'max_length': '650'})
        },
        u'location.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '650'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'id_location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['location.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        },
        u'location.location': {
            'Meta': {'object_name': 'Location'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '650'}),
            'id_location': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'location.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '650'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'id_location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['location.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        },
        u'location.sport': {
            'Meta': {'object_name': 'Sport'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '650'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'id_location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['location.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '650'})
        }
    }

    complete_apps = ['location']