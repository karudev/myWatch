from service.flux_service import FluxService

fluxService = FluxService('tests/mocks/data.xml')
#fluxService.get_data('/users/user/nom')
#fluxService = FluxService('http://www.lemonde.fr/technologies/rss_full.xml')
#fluxService.get_data('/rss/channel/item')
fluxService.parseXML('user')


if __name__ == 'main' :
    main()