from home.models import Team, Portfolio, Total, HomeTitle
from footer.models import FooterLogoMeta, FooterMenusMeta, FooterContactsMeta, FooterServicesMeta


def footerlogoview(request):
    meta_footer_latest = FooterLogoMeta.objects.all().order_by('-id')[:1]
    context = {
        'meta_footer_latest': meta_footer_latest,
    }
    return context


def footermenusview(request):
    footer_menus_latest = FooterMenusMeta.objects.all().order_by('-id')[:10]
    context = {
        'footer_menus_latest': footer_menus_latest,
    }
    return context


def footercontactsview(request):
    footer_contacts_latest = FooterContactsMeta.objects.all().order_by('-id')[:1]
    context = {
        'footer_contacts_latest': footer_contacts_latest,
    }
    return context


def footerservicesview(request):
    footer_services_latest = FooterServicesMeta.objects.all().order_by('-id')[:10]
    context = {
        'footer_services_latest': footer_services_latest,
    }
    return context


def total(request):
    total_latest = Total.objects.all().order_by('-id')[:1]
    context = {
        'total_latest': total_latest,
    }
    return context


def teamview(request):
    team_latest = Team.objects.all().order_by('-id')[:25]
    context = {
        'team_latest': team_latest,
    }
    return context


def portfolioview(request):
    portfolio_latest = Portfolio.objects.all().order_by('-id')[:25]
    context = {
        'portfolio_latest': portfolio_latest,
    }
    return context


def hometitle(request):
    home_title_latest = HomeTitle.objects.all().order_by('-id')[:1]
    context = {
        'home_title_latest': home_title_latest,
    }
    return context
