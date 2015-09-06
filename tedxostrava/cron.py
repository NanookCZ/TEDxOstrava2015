import urllib
from push_notifications.models import APNSDevice, GCMDevice


def my_scheduled_job():
	device = GCMDevice.objects.get(registration_id=gcm_reg_id)
	device.send_message(None, extra={"foo": "bar"})
	device = APNSDevice.objects.get(registration_id=apns_token)
	device.send_message(None, badge=1, extra={"foo": "bar"})