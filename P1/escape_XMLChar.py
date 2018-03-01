def xml_Escape (m):	

	m=m.replace('&quot;','"')
	m=m.replace('&amp;','&')
	m=m.replace('&apos;','\'')
	m=m.replace('&lt;','<')
	m=m.replace('&gt;','>')
	m=m.replace('&nbsp;','')
	m=m.replace('&iexcl;','¡')
	m=m.replace('&cent;','¢')
	m=m.replace('&pound;','£')
	m=m.replace('&curren;','¤')
	m=m.replace('&yen;','¥')
	m=m.replace('&brvbar;','¦')
	m=m.replace('&sect;','§')
	m=m.replace('&uml;','¨')
	m=m.replace('&copy;','©')
	m=m.replace('&ordf;','ª')
	m=m.replace('&laquo;','«')
	m=m.replace('&not;','¬')
	m=m.replace('&shy;','')
	m=m.replace('&reg;','®')
	m=m.replace('&macr;','¯')
	m=m.replace('&deg;','°')
	m=m.replace('&plusmn;','±')
	m=m.replace('&sup2;','²')
	m=m.replace('&sup3;','³')
	m=m.replace('&acute;','´')
	m=m.replace('&micro;','µ')
	m=m.replace('&para;','¶')
	m=m.replace('&middot;','·')
	m=m.replace('&cedil;','¸')
	m=m.replace('&sup1;','¹')
	m=m.replace('&ordm;','º')
	m=m.replace('&raquo;','»')
	m=m.replace('&frac14;','¼')
	m=m.replace('&frac12;','½')
	m=m.replace('&frac34;','¾')
	m=m.replace('&iquest;','¿')
	m=m.replace('&Agrave;','À')
	m=m.replace('&Aacute;','Á')
	m=m.replace('&Acirc;','Â')
	m=m.replace('&Atilde;','Ã')
	m=m.replace('&Auml;','Ä')
	m=m.replace('&Aring;','Å')
	m=m.replace('&AElig;','Æ')
	m=m.replace('&Ccedil;','Ç')
	m=m.replace('&Egrave;','È')
	m=m.replace('&Eacute;','É')
	m=m.replace('&Ecirc;','Ê')
	m=m.replace('&Euml;','Ë')
	m=m.replace('&Igrave;','Ì')
	m=m.replace('&Iacute;','Í')
	m=m.replace('&Icirc;','Î')
	m=m.replace('&Iuml;','Ï')
	m=m.replace('&ETH;','Ð')
	m=m.replace('&Ntilde;','Ñ')
	m=m.replace('&Ograve;','Ò')
	m=m.replace('&Oacute;','Ó')
	m=m.replace('&Ocirc;','Ô')
	m=m.replace('&Otilde;','Õ')
	m=m.replace('&Ouml;','Ö')
	m=m.replace('&times;','×')
	m=m.replace('&Oslash;','Ø')
	m=m.replace('&Ugrave;','Ù')
	m=m.replace('&Uacute;','Ú')
	m=m.replace('&Ucirc;','Û')
	m=m.replace('&Uuml;','Ü')
	m=m.replace('&Yacute;','Ý')
	m=m.replace('&THORN;','Þ')
	m=m.replace('&szlig;','ß')
	m=m.replace('&agrave;','à')
	m=m.replace('&aacute;','á')
	m=m.replace('&acirc;','â')
	m=m.replace('&atilde;','ã')
	m=m.replace('&auml;','ä')
	m=m.replace('&aring;','å')
	m=m.replace('&aelig;','æ')
	m=m.replace('&ccedil;','ç')
	m=m.replace('&egrave;','è')
	m=m.replace('&eacute;','é')
	m=m.replace('&ecirc;','ê')
	m=m.replace('&euml;','ë')
	m=m.replace('&igrave;','ì')
	m=m.replace('&iacute;','í')
	m=m.replace('&icirc;','î')
	m=m.replace('&iuml;','ï')
	m=m.replace('&eth;','ð')
	m=m.replace('&ntilde;','ñ')
	m=m.replace('&ograve;','ò')
	m=m.replace('&oacute;','ó')
	m=m.replace('&ocirc;','ô')
	m=m.replace('&otilde;','õ')
	m=m.replace('&ouml;','ö')
	m=m.replace('&divide;','÷')
	m=m.replace('&oslash;','ø')
	m=m.replace('&ugrave;','ù')
	m=m.replace('&uacute;','ú')
	m=m.replace('&ucirc;','û')
	m=m.replace('&uuml;','ü')
	m=m.replace('&yacute;','ý')
	m=m.replace('&thorn;','þ')
	m=m.replace('&yuml;','ÿ')
	m=m.replace('&OElig;','Œ')
	m=m.replace('&oelig;','œ')
	m=m.replace('&Scaron;','Š')
	m=m.replace('&scaron;','š')
	m=m.replace('&Yuml;','Ÿ')
	m=m.replace('&fnof;','ƒ')
	m=m.replace('&circ;','ˆ')
	m=m.replace('&tilde;','˜')
	m=m.replace('&Alpha;','Α')
	m=m.replace('&Beta;','Β')
	m=m.replace('&Gamma;','Γ')
	m=m.replace('&Delta;','Δ')
	m=m.replace('&Epsilon;','Ε')
	m=m.replace('&Zeta;','Ζ')
	m=m.replace('&Eta;','Η')
	m=m.replace('&Theta;','Θ')
	m=m.replace('&Iota;','Ι')
	m=m.replace('&Kappa;','Κ')
	m=m.replace('&Lambda;','Λ')
	m=m.replace('&Mu;','Μ')
	m=m.replace('&Nu;','Ν')
	m=m.replace('&Xi;','Ξ')
	m=m.replace('&Omicron;','Ο')
	m=m.replace('&Pi;','Π')
	m=m.replace('&Rho;','Ρ')
	m=m.replace('&Sigma;','Σ')
	m=m.replace('&Tau;','Τ')
	m=m.replace('&Upsilon;','Υ')
	m=m.replace('&Phi;','Φ')
	m=m.replace('&Chi;','Χ')
	m=m.replace('&Psi;','Ψ')
	m=m.replace('&Omega;','Ω')
	m=m.replace('&alpha;','α')
	m=m.replace('&beta;','β')
	m=m.replace('&gamma;','γ')
	m=m.replace('&delta;','δ')
	m=m.replace('&epsilon;','ε')
	m=m.replace('&zeta;','ζ')
	m=m.replace('&eta;','η')
	m=m.replace('&theta;','θ')
	m=m.replace('&iota;','ι')
	m=m.replace('&kappa;','κ')
	m=m.replace('&lambda;','λ')
	m=m.replace('&mu;','μ')
	m=m.replace('&nu;','ν')
	m=m.replace('&xi;','ξ')
	m=m.replace('&omicron;','ο')
	m=m.replace('&pi;','π')
	m=m.replace('&rho;','ρ')
	m=m.replace('&sigmaf;','ς')
	m=m.replace('&sigma;','σ')
	m=m.replace('&tau;','τ')
	m=m.replace('&upsilon;','υ')
	m=m.replace('&phi;','φ')
	m=m.replace('&chi;','χ')
	m=m.replace('&psi;','ψ')
	m=m.replace('&omega;','ω')
	m=m.replace('&thetasym;','ϑ')
	m=m.replace('&upsih;','ϒ')
	m=m.replace('&piv;','ϖ')
	m=m.replace('&ensp;',' ')
	m=m.replace('&emsp;',' ')
	m=m.replace('&thinsp;',' ')
	m=m.replace('&zwnj;','')
	m=m.replace('&zwj;','')
	m=m.replace('&lrm;','')
	m=m.replace('&rlm;','')
	m=m.replace('&ndash;','–')
	m=m.replace('&mdash;','—')
	m=m.replace('&lsquo;','‘')
	m=m.replace('&rsquo;','’')
	m=m.replace('&sbquo;','‚')
	m=m.replace('&ldquo;','“')
	m=m.replace('&rdquo;','”')
	m=m.replace('&bdquo;','„')
	m=m.replace('&dagger;','†')
	m=m.replace('&Dagger;','‡')
	m=m.replace('&bull;','•')
	m=m.replace('&hellip;','…')
	m=m.replace('&permil;','‰')
	m=m.replace('&prime;','′')
	m=m.replace('&Prime;','″')
	m=m.replace('&lsaquo;','‹')
	m=m.replace('&rsaquo;','›')
	m=m.replace('&oline;','‾')
	m=m.replace('&frasl;','⁄')
	m=m.replace('&euro;','€')
	m=m.replace('&image;','ℑ')
	m=m.replace('&weierp;','℘')
	m=m.replace('&real;','ℜ')
	m=m.replace('&trade;','™')
	m=m.replace('&alefsym;','ℵ')
	m=m.replace('&larr;','←')
	m=m.replace('&uarr;','↑')
	m=m.replace('&rarr;','→')
	m=m.replace('&darr;','↓')
	m=m.replace('&harr;','↔')
	m=m.replace('&crarr;','↵')
	m=m.replace('&lArr;','⇐')
	m=m.replace('&uArr;','⇑')
	m=m.replace('&rArr;','⇒')
	m=m.replace('&dArr;','⇓')
	m=m.replace('&hArr;','⇔')
	m=m.replace('&forall;','∀')
	m=m.replace('&part;','∂')
	m=m.replace('&exist;','∃')
	m=m.replace('&empty;','∅')
	m=m.replace('&nabla;','∇')
	m=m.replace('&isin;','∈')
	m=m.replace('&notin;','∉')
	m=m.replace('&ni;','∋')
	m=m.replace('&prod;','∏')
	m=m.replace('&sum;','∑')
	m=m.replace('&minus;','−')
	m=m.replace('&lowast;','∗')
	m=m.replace('&radic;','√')
	m=m.replace('&prop;','∝')
	m=m.replace('&infin;','∞')
	m=m.replace('&ang;','∠')
	m=m.replace('&and;','∧')
	m=m.replace('&or;','∨')
	m=m.replace('&cap;','∩')
	m=m.replace('&cup;','∪')
	m=m.replace('&int;','∫')
	m=m.replace('&there4;','∴')
	m=m.replace('&sim;','∼')
	m=m.replace('&cong;','≅')
	m=m.replace('&asymp;','≈')
	m=m.replace('&ne;','≠')
	m=m.replace('&equiv;','≡')
	m=m.replace('&le;','≤')
	m=m.replace('&ge;','≥')
	m=m.replace('&sub;','⊂')
	m=m.replace('&sup;','⊃')
	m=m.replace('&nsub;','⊄')
	m=m.replace('&sube;','⊆')
	m=m.replace('&supe;','⊇')
	m=m.replace('&oplus;','⊕')
	m=m.replace('&otimes;','⊗')
	m=m.replace('&perp;','⊥')
	m=m.replace('&sdot;','⋅')
	m=m.replace('&vellip;','⋮')
	m=m.replace('&lceil;','⌈')
	m=m.replace('&rceil;','⌉')
	m=m.replace('&lfloor;','⌊')
	m=m.replace('&rfloor;','⌋')
	m=m.replace('&lang;','〈')
	m=m.replace('&rang;','〉')
	m=m.replace('&loz;','◊')
	m=m.replace('&spades;','♠')
	m=m.replace('&clubs;','♣')
	m=m.replace('&hearts;','♥')
	m=m.replace('&diams;','♦')
	
	return m