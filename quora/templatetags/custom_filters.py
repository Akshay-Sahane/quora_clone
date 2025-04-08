from django import template

register = template.Library()


@register.filter
def has_upvoted(upvotes, user):
    if upvotes:
        return upvotes.filter(upvoted_by=user, is_active=True).exists()
    return False

@register.filter
def get_active_count(upvotes):
    if upvotes:
        return upvotes.filter(is_active=True).count()
    return 0


@register.filter
def has_answered(question, user):
    return question.answers.filter(created_by=user).exists()