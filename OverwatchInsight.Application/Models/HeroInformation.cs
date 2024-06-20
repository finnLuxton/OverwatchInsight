using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OverwatchInsight.Application.Models;

public record HeroInformation
(
    string HeroName,
    List<string> StrongAgainst,
    List<string> GoodAgainst,
    List<string> WeakAgainst,
    List<string> BadAgainst
); 