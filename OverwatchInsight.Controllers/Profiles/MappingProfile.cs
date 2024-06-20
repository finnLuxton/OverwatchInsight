using AutoMapper;

namespace OverwatchInsight.Controller.Profiles;

public class MappingProfile : Profile
{
    public MappingProfile()
    {
        CreateMap<Application.Models.HeroMatchup, Models.HeroMatchup>();
    }
}

