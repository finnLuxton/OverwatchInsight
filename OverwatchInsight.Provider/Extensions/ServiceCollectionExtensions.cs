using Microsoft.Extensions.DependencyInjection;
using OverwatchInsight.Application.Contracts.Outbound;

namespace OverwatchInsight.Provider.Extensions;

//TODO : What does internal class do differently from public static class?
public static class ServiceCollectionExtensions
{
    public static void AddProviderServices(this IServiceCollection services)
    {
        services.AddScoped<IHeroInformationProvider, HeroInformationProvider>();
    }

}

