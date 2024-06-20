using Microsoft.Extensions.DependencyInjection;
using OverwatchInsight.Application.Contracts.Outbound;

namespace OverwatchInsight.Provider.Startup;

//TODO : What does internal class do differently from public static class?
public static class DependencyInjection
{
    public static void RegisterServices(IServiceCollection services)
    {
        services.AddScoped<IHeroInformationProvider, HeroInformationProvider>();    
    }

}

