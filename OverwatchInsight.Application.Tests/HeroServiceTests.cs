using FluentAssertions;
using Moq;
using AutoFixture;
using Xunit;
using OverwatchInsight.Application.Contracts.Inbound;
using OverwatchInsight.Application.Services;
using OverwatchInsight.Application.Contracts.Outbound;
using OverwatchInsight.Application.Models;

namespace OverwatchInsight.Application.Tests
{
    public class HeroServiceTests
    {
        private readonly IHeroServiceProvider _serviceProvider;
        private readonly Mock<IHeroInformationProvider> _heroInformationProviderMock;
        private Fixture _fixture;

        public HeroServiceTests()
        {
            _heroInformationProviderMock = new Mock<IHeroInformationProvider>();
            _serviceProvider = new HeroService(_heroInformationProviderMock.Object);
            _fixture = new Fixture();
        }

        [Fact]
        public async Task GivenListOfEnemyHeroes_WhenCallingGetHeroMatchup_ReturnListOfHeroMatchups()
        {
            // Arrange
            var enemyHeroList = new List<String>();
            enemyHeroList.Add(_fixture.Create<string>());

            var heroInformationList = new List<HeroInformation>();
            heroInformationList.Add(_fixture.Create<HeroInformation>());

            _heroInformationProviderMock.Setup(x => x.GetHeroInformation()).ReturnsAsync(heroInformationList);

            // Act
            var result = await _serviceProvider.GetHeroMatchup(enemyHeroList);

            // Assert
            result.Should().NotBeNull();
            result.Should().BeOfType<List<HeroMatchup>>();
        }
    }
}