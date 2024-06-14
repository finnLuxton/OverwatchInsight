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

    public Task<HeroMatchup> GetHeroMatchup(List<String> Heroes)
    {
        return Task.FromResult(new HeroMatchup("Torbjorn", 0));
    }
}

