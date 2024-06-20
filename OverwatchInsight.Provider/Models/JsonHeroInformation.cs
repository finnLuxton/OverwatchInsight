using System.Text.Json;
using Newtonsoft.Json;
using OverwatchInsight.Application.Models;

namespace OverwatchInsight.Provider.Models;

public record JsonHeroInformation(
    [property: JsonProperty("HeroName")] string HeroName,
    [property: JsonProperty("StrongAgainst")] List<string> StrongAgainst,
    [property: JsonProperty("GoodAgainst")] List<string> GoodAgainst,
    [property: JsonProperty("WeakAgainst")] List<string> WeakAgainst,
    [property: JsonProperty("BadAgainst")] List<string> BadAgainst
)
{
    public HeroInformation MapToHeroInformation()
    => new(
        HeroName,
        StrongAgainst,
        GoodAgainst,
        WeakAgainst,
        BadAgainst);
}
