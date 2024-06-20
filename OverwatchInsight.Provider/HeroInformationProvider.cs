using OverwatchInsight.Provider.Models;
using OverwatchInsight.Application.Models;
using OverwatchInsight.Application.Contracts.Outbound;
using System.Text.Json;

namespace OverwatchInsight.Provider;

public class HeroInformationProvider : IHeroInformationProvider
{
    public async Task<List<HeroInformation>> GetHeroInformation()
    {
        // TODO: Fix this not being a hardcoded file path
        string jsonString = await File.ReadAllTextAsync("overwatch_heroes.json");

        List<JsonHeroInformation> jsonHeroInformation = JsonSerializer.Deserialize<List<JsonHeroInformation>>(jsonString);

        List<HeroInformation> heroInformation = jsonHeroInformation?.Select(jsonHero => jsonHero.MapToHeroInformation()).ToList();

        return heroInformation;
    }
}

