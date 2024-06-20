using OverwatchInsight.Application.Contracts.Inbound;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OverwatchInsight.Application.Models;
using OverwatchInsight.Application.Contracts.Outbound;

namespace OverwatchInsight.Application.Services;

public class HeroService : IHeroServiceProvider
{
    private readonly IHeroInformationProvider _heroInformationProvider;

    public HeroService(IHeroInformationProvider heroInformationProvider)
    {
        _heroInformationProvider = heroInformationProvider ?? throw new ArgumentNullException(nameof(heroInformationProvider));
    }

    public Task<List<HeroMatchup>> GetHeroMatchup(List<String> Heroes)
    {
        var heroMatchupList = new List<HeroMatchup>
        {
            new HeroMatchup("Torbjorn", 0)
        };

        var output = _heroInformationProvider.GetHeroInformation();

        return Task.FromResult(heroMatchupList);
    }
}

