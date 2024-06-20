using OverwatchInsight.Application.Models;

namespace OverwatchInsight.Application.Contracts.Outbound;
public interface IHeroInformationProvider
{
    Task<List<HeroInformation>> GetHeroInformation();
}

