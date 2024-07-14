using OverwatchInsight.Application.Contracts.Inbound;
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
        var heroInformation = await _heroInformationProvider.GetHeroInformation();

        var heroMatchups = new List<HeroMatchup>();

        // TODO Extract this out to a function.
        // TODO: Look into also processing player team heroes?
        // TODO: Alice supplied reasonings for matchups. Maybe look at incorporating into output?
        foreach (HeroInformation hero in heroInformation)
        {
            int matchupValue = 0;

            foreach (var enemyHero in EnemyHeroes)
            {
                var lowerHero = enemyHero.ToLower();
                if (hero.StrongAgainst.Contains(lowerHero))
                    matchupValue += 5;

                if (hero.GoodAgainst.Contains(lowerHero))
                    matchupValue += 2;

                if (hero.WeakAgainst.Contains(lowerHero))
                    matchupValue += -2;

                if (hero.BadAgainst.Contains(lowerHero))
                    matchupValue += -5;
            }

            heroMatchups.Add(new HeroMatchup(
                        HeroName: hero.HeroName,
                        MatchupValue: matchupValue));
        }

        return heroMatchups;
    }
}

