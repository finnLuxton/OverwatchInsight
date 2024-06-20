using OverwatchInsight.Application.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OverwatchInsight.Application.Contracts.Inbound;
public interface IHeroServiceProvider
{
    Task<List<HeroMatchup>> GetHeroMatchup(List<string> Heroes); // TODO: This is not the correct parameter type. Make it different for uncoupling

}

