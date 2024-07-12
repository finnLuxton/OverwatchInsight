using AutoMapper;
using OverwatchInsight.Application.Contracts.Inbound;
using OverwatchInsight.Controller.Profiles;
using Xunit;
using Moq;
using AutoFixture;
using OverwatchInsight.Application.Models;
using FluentAssertions;
using Microsoft.AspNetCore.Mvc;


namespace OverwatchInsight.Controllers.Tests
{
    public class HeroControllerTests
    {
        public readonly Mock<IHeroServiceProvider> _serviceProviderMock;
        public readonly HeroController _heroController;
        public readonly Fixture _fixture;

        public HeroControllerTests()
        {
            var mapperConfig = new MapperConfiguration(config =>
            {
                config.AddProfile<MappingProfile>();
            });
            _serviceProviderMock = new Mock<IHeroServiceProvider>();
            _fixture = new Fixture();
            _heroController = new HeroController(mapperConfig.CreateMapper(), _serviceProviderMock.Object);
        }

        [Fact]
        public async Task WhenCallingGetHeroAsync_IfPassingHeroList_ReturnMappedHeroMatchup()
        {
            // Arrange
            var heroList = new List<String>()
            {
                "Widowmaker",
                "Torbjorn",
                "Ana"
            };
            var heroMatchup = new List<HeroMatchup>();
            heroMatchup.Add(_fixture.Create<HeroMatchup>());
            _serviceProviderMock.Setup(x => x.GetHeroMatchup(heroList)).ReturnsAsync(heroMatchup);

            // Act
            var actionResult = await _heroController.GetHeroAsync(heroList);

            // Assert
            var result = actionResult.Result as OkObjectResult; // Adjusted to handle ActionResult<T>
            result.Should().NotBeNull();
            result.Value.Should().BeEquivalentTo(heroMatchup);
        }
    }
}
