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

    public async Task<List<HeroMatchup>> GetHeroMatchup(List<String> EnemyHeroes)
    {
        // Outputs list of all heroes, and their matchup scores.
        var heroInformation = await _heroInformationProvider.GetHeroInformation();

        var heroMatchups = new List<HeroMatchup>();

        //string HeroName,
        //List<string> StrongAgainst,
        //List<string> GoodAgainst,
        //List<string> WeakAgainst,
        //List<string> BadAgainst

        // TODO Extract this out to a function.
        foreach (HeroInformation hero in heroInformation)
        {
            heroMatchups.Add(new HeroMatchup(
                                    HeroName: hero.HeroName,
                                    MatchupValue: 0));

        }

        // For each hero in JsonFileOutput
        // // For each against attribute
        // // // Check if agaisnt attribute is empty
        // // // If not empty, iterate through EnemyHeroes parameter.
        // // // // If EnemyHeroes exists within attribute, adjust HeroMatchup.MatchupScore value

        // E.G We have an enemy hero parameter of Winston.
        // The JsonHeroMatchup for Reaper has Winston as StrongAgaisnt, and Genji as BadAgaisnt, and Soldier 76 as nothing.
        // The JsonHeroMatchup will give Reaper +5 Matchup score, and Genji -5, and Soldier has no change.

        return heroMatchups;
    }
}

