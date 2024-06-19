using System.Collections.Generic;
using System.Threading.Tasks;
using AutoMapper;
using Moq;
using OverwatchInsight.Application.Contracts.Outbound;
using OverwatchInsight.Controllers;
using Xunit;

namespace OverwatchInsight.Tests
{
    public class HeroControllerTests
    {
        private readonly Mock<IMapper> _mockMapper;
        private readonly Mock<IHeroServiceProvider> _mockHeroServiceProvider;
        private readonly HeroController _controller;

        public HeroControllerTests()
        {
            _mockMapper = new Mock<IMapper>();
            _mockHeroServiceProvider = new Mock<IHeroServiceProvider>();
            _controller = new HeroController(_mockMapper.Object, _mockHeroServiceProvider.Object);
        }

        //[Fact]
        //public async Task GivenValidInput_WhenCallingGetHeroAsync_GetHeroMatchupOutput()
        //{
        //    // Arrange
        //    var enemyHeroes = new List<string> { "Reinhardt", "Zarya" };
        //    var expectedHeroName = "Torbjorn";
        //    var heroMatchup = new HeroMatchup(expectedHeroName, 0);

        //    _mockHeroServiceProvider.Setup(s => s.GetHeroMatchup(It.IsAny<List<string>>()))
        //        .Returns(Task.FromResult(heroMatchup));

        //    // Act
        //    var result = await _controller.GetHeroAsync(enemyHeroes);

        //    // Assert
        //    Assert.Equal(expectedHeroName, result);
        //}
    }
}