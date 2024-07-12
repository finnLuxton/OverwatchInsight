using OverwatchInsight.Application.Models;
using FluentAssertions;
using OverwatchInsight.Application.Contracts.Outbound;

namespace OverwatchInsight.Provider.Tests
{
    public class HeroControllerTests
    {
        public readonly IHeroInformationProvider _heroInformationProvider;
        
        public HeroControllerTests()
        {
            _heroInformationProvider = new HeroInformationProvider();
        }

        [Fact]
        public async Task WhenCallingGetHeroInformation_GetListOfHeroInformation()
        {
            // Act
            var result = await _heroInformationProvider.GetHeroInformation();

            // Assert
            result.Should().BeOfType<List<HeroInformation>>();
        }
    }
}
