using OverwatchInsight.Application.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OverwatchInsight.Application.Contracts.Outbound;
public interface IHeroServiceProvider
{
    Task<HeroMatchup> GetHeroMatchup(List<String> Heroes); // TODO: This is not the correct parameter type. Make it different for uncoupling

}

