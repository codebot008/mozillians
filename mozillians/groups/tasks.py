from django.db.models import Count

from celery.task import task

from mozillians.groups.models import Group, Skill


@task
def remove_empty_groups():
    """Remove empty groups."""
    for model in [Group, Skill]:
        (model.objects
         .annotate(mcount=Count('members')).filter(mcount=0).delete())
