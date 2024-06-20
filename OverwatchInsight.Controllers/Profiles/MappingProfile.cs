using AutoMapper;
using OverwatchInsight.Models; // TODO Cleanup the namespacing issues here
using OverwatchInsight.Application.Models;

namespace OverwatchInsight.Controllers.Profiles
{
    public class MappingProfile : Profile
    {
        public MappingProfile()
        {
            CreateMap<Application.Models.HeroMatchup, Models.HeroMatchup>();
        }
    }
}
