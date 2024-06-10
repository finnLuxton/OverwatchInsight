using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using OverwatchInsight.Models;

namespace OverwatchInsight.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class HeroController : ControllerBase
    {
        // TODO: Look into DI Data model here

        [HttpGet]
        [Route("GetHeroMatchup")]
        public async Task<IList<HeroMatchup>> GetHeroAsync([FromQuery]IList<String> EnemyHeroes) // TODO: See if there is a better way for postman to format list of query inputs
        {
            return new List<HeroMatchup>
                {
                    new HeroMatchup("Reinhardt", 100), new HeroMatchup("Zarya", 90)
            };
        }

    }
}
