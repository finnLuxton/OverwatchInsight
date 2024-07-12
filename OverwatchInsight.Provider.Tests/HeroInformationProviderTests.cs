using OverwatchInsight.Application.Models;
using FluentAssertions;
using OverwatchInsight.Application.Contracts.Outbound;
using Xunit;

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
            result.Should().NotBeNull();
            result.Should().BeOfType<List<HeroInformation>>();
        }
    }
}
