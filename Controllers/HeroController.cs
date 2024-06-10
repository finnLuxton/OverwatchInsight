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
        [Route("getHeroMatchup")]
        public async Task<HeroMatchup> GetHeroAsync()
        {
            return new HeroMatchup("Reinhardt", 100);
        }

    }
}
