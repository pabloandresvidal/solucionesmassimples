# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cotizador'
        db.create_table(u'core_cotizador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Ciudad'])),
            ('barrio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Barrio'])),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('mensaje', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Cotizador'])

        # Adding M2M table for field categoria on 'Cotizador'
        m2m_table_name = db.shorten_name(u'core_cotizador_categoria')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cotizador', models.ForeignKey(orm[u'core.cotizador'], null=False)),
            ('categoria', models.ForeignKey(orm[u'core.categoria'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cotizador_id', 'categoria_id'])

        # Adding model 'Categoria'
        db.create_table(u'core_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'core', ['Categoria'])

        # Adding model 'Barrio'
        db.create_table(u'core_barrio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('barrio', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'core', ['Barrio'])

        # Adding model 'Ciudad'
        db.create_table(u'core_ciudad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'core', ['Ciudad'])

        # Adding model 'Trabajo'
        db.create_table(u'core_trabajo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('id_servicio', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre_servicio', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('diagnostico_previo', self.gf('django.db.models.fields.TextField')()),
            ('solucion', self.gf('django.db.models.fields.TextField')()),
            ('cotizacion', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_creacion', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Trabajo'])

        # Adding model 'ReporteDiario'
        db.create_table(u'core_reportediario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('trabajo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Trabajo'])),
            ('report', self.gf('django.db.models.fields.TextField')()),
            ('foto1', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('foto2', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('foto3', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('foto4', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['ReporteDiario'])

        # Adding model 'ItemCotizacion'
        db.create_table(u'core_itemcotizacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trabajo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Trabajo'])),
            ('item', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('valor', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'core', ['ItemCotizacion'])


    def backwards(self, orm):
        # Deleting model 'Cotizador'
        db.delete_table(u'core_cotizador')

        # Removing M2M table for field categoria on 'Cotizador'
        db.delete_table(db.shorten_name(u'core_cotizador_categoria'))

        # Deleting model 'Categoria'
        db.delete_table(u'core_categoria')

        # Deleting model 'Barrio'
        db.delete_table(u'core_barrio')

        # Deleting model 'Ciudad'
        db.delete_table(u'core_ciudad')

        # Deleting model 'Trabajo'
        db.delete_table(u'core_trabajo')

        # Deleting model 'ReporteDiario'
        db.delete_table(u'core_reportediario')

        # Deleting model 'ItemCotizacion'
        db.delete_table(u'core_itemcotizacion')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.barrio': {
            'Meta': {'object_name': 'Barrio'},
            'barrio': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.cotizador': {
            'Meta': {'object_name': 'Cotizador'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'barrio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Barrio']"}),
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Categoria']", 'symmetrical': 'False'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Ciudad']"}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensaje': ('django.db.models.fields.TextField', [], {}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.itemcotizacion': {
            'Meta': {'object_name': 'ItemCotizacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'trabajo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Trabajo']"}),
            'valor': ('django.db.models.fields.IntegerField', [], {})
        },
        u'core.reportediario': {
            'Meta': {'object_name': 'ReporteDiario'},
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'foto1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'foto2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto4': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.TextField', [], {}),
            'trabajo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Trabajo']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'core.trabajo': {
            'Meta': {'object_name': 'Trabajo'},
            'cotizacion': ('django.db.models.fields.IntegerField', [], {}),
            'diagnostico_previo': ('django.db.models.fields.TextField', [], {}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_servicio': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'nombre_servicio': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'solucion': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['core']