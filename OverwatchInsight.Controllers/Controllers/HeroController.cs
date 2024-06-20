using AutoMapper;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using OverwatchInsight.Application.Contracts.Inbound;
using OverwatchInsight.Application.Services;
using OverwatchInsight.Models;

namespace OverwatchInsight.Controllers;

[Route("api/[controller]")]
[ApiController]
public class HeroController : ControllerBase
{
    // TODO: Look into DI Data model here
    private readonly IMapper _mapper;
    private readonly IHeroServiceProvider _heroServiceProvider;

    public HeroController(IMapper mapper, IHeroServiceProvider heroServiceProvider)
    {
        _heroServiceProvider = heroServiceProvider ?? throw new ArgumentNullException(nameof(heroServiceProvider));
        _mapper = mapper ?? throw new ArgumentNullException(nameof(mapper));
    }

    [HttpGet]
    [Route("GetHeroMatchup")]
    public async Task<ActionResult<List<HeroMatchup>>> GetHeroAsync([FromQuery]List<String> EnemyHeroes) // TODO: See if there is a better way for postman to format list of query inputs
    {
        var result = await _heroServiceProvider.GetHeroMatchup(EnemyHeroes);

        var mappedResult = _mapper.Map<List<HeroMatchup>>(result);
        return Ok(mappedResult);
    }

}

