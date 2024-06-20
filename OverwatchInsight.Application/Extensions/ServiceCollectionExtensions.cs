using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Extensions.DependencyInjection;
using OverwatchInsight.Application.Services;
using OverwatchInsight.Application.Contracts.Inbound;

namespace OverwatchInsight.Application.Extensions;
public static class ServiceCollectionExtensions
{
    public static void AddApplicationServices(this IServiceCollection services)
    {
        services.AddScoped<IHeroServiceProvider, HeroService>();
    }
}

